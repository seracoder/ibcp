import asyncio

import httpx

from ibcp.models import (
    Account,
    AuthStatusResponse,
    CancelOrderResponse,
    CashBalanceResponse,
    CurrencyValue,
    FuturesContract,
    LiveOrder,
    LiveOrdersResponse,
    LogoutResponse,
    MarketDataSnapshot,
    MarketHistoryResponse,
    NetValueResponse,
    OrderConfirmationMessage,
    OrderReplyItem,
    OrderStatus,
    PortfolioPosition,
    PortfolioResponse,
    ReauthenticateResponse,
    StockInstrument,
    SwitchAccountResponse,
    TickleResponse,
    User
)

__all__ = ["REST"]


class REST:
    """Allows to send REST API requests to Interactive Brokers Client Portal Web API.

    :param url: Gateway session link, defaults to "https://localhost:5000"
    :type url: str, optional
    :param ssl: Usage of SSL certificate, defaults to False
    :type ssl: bool, optional
    """

    def __init__(self, url="https://localhost:5000", ssl=False) -> None:
        """Create a new instance to interact with REST API

        :param url: Gateway session link, defaults to "https://localhost:5000"
        :type url: str, optional
        :param ssl: Usage of SSL certificate, defaults to False
        :type ssl: bool, optional
        """
        self.url = f"{url}/v1/api"
        self._account_id = None
        self._client = httpx.AsyncClient(verify=ssl, http2=True)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

    async def close(self):
        """Close the underlying HTTP client."""
        if self._client is not None:
            await self._client.aclose()
            self._client = None

    @property
    def client(self) -> httpx.AsyncClient:
        if self._client is None:
            raise RuntimeError("Client has been closed. Create a new REST instance.")
        return self._client

    def _require_account_id(self, account_id=None) -> str:
        resolved = account_id or self._account_id
        if resolved is None:
            raise RuntimeError(
                "No account ID set. Call set_default_account() first or pass account_id."
            )
        return resolved

    async def set_default_account(self, account_id=None) -> str:
        """Set the default account ID.

        If account_id is provided, it is used directly without making a request.
        Otherwise, fetches accounts from the server and uses the first one.

        :param account_id: Optional account ID to set directly, defaults to None
        :type account_id: str, optional
        :return: The account ID that was set
        :rtype: str
        """
        if account_id is not None:
            self._account_id = account_id
        else:
            accounts = await self.get_accounts()
            self._account_id = accounts[0].account_id
        return self._account_id

    async def get_user(self) -> User:
        """Returns user info"""
        response = await self.client.get(f"{self.url}/v1/api/one/user")
        return User(**response.json())

    async def get_accounts(self) -> list[Account]:
        """Returns account info

        :return: list of account info
        :rtype: list[Account]
        """
        response = await self.client.get(f"{self.url}/portfolio/accounts")
        return [Account(**item) for item in response.json()]

    async def switch_account(self, account_id: str) -> SwitchAccountResponse:
        """Switch selected account to the input account

        :param account_id: account ID of the desired account
        :type account_id: str
        :return: Response from the server
        :rtype: SwitchAccountResponse
        """
        response = await self.client.post(
            f"{self.url}/iserver/account", json={"acctId": account_id}
        )
        self._account_id = account_id
        return SwitchAccountResponse(**response.json())

    async def get_cash_balance(
        self, account_id=None, currency=None
    ) -> CashBalanceResponse:
        """Returns cash balance of the selected account

        :param account_id: Account ID, uses default if not provided
        :type account_id: str, optional
        :param currency: Currency to return
        :type currency: str, optional
        :return: dict of cash balance
        :rtype: CashBalanceResponse
        """
        aid = self._require_account_id(account_id)
        response = await self.client.get(f"{self.url}/portfolio/{aid}/ledger")
        body = response.json()

        items: list[CurrencyValue] = []
        if currency:
            items.append(
                CurrencyValue(currency=currency, value=body[currency]["cashbalance"])
            )
        else:
            items = [
                CurrencyValue(currency=key, value=item["cashbalance"])
                for key, item in body.items()
                if key != "BASE"
            ]
        return CashBalanceResponse(items=items)

    async def get_stock_last_price(
        self,
        ticker: str,
        conid: str | int = "default",
        contract_filters=None,
    ) -> float:
        """Get the last price of a stock

        :param ticker: The ticker of the stock
        :type ticker: str
        :param conid: Contract ID, defaults to "default"
        :type conid: str or int, optional
        :param contract_filters: Key-value pair of filters, defaults to {"isUS": True}
        :type contract_filters: dict, optional
        :return: Last stock price
        :rtype: float
        """
        if contract_filters is None:
            contract_filters = {"isUS": True}

        price = None
        while price is None:
            try:
                response = await self.get_marketdata_snapshot(
                    ticker, conid, contract_filters=contract_filters
                )
                price = response[0].model_extra["31"]
            except Exception:
                print(f"Waiting for {ticker} price")
                await asyncio.sleep(0.5)

        return float(price.replace("C", ""))

    async def get_netvalue(self, account_id=None, currency=None) -> NetValueResponse:
        """Returns net value of the selected account

        :param account_id: Account ID, uses default if not provided
        :type account_id: str, optional
        :param currency: Currency to return
        :type currency: str, optional
        :return: Net value of the selected account
        :rtype: NetValueResponse
        """
        aid = self._require_account_id(account_id)
        response = await self.client.get(f"{self.url}/portfolio/{aid}/ledger")
        body = response.json()

        items: list[CurrencyValue] = []
        if currency:
            items.append(
                CurrencyValue(
                    currency=currency, value=body[currency]["netliquidationvalue"]
                )
            )
        else:
            items = [
                CurrencyValue(currency=key, value=item["netliquidationvalue"])
                for key, item in body.items()
                if key != "BASE"
            ]
        return NetValueResponse(items=items)

    async def get_conid(
        self,
        symbol: str,
        instrument_filters=None,
        contract_filters=None,
    ) -> int:
        """Returns contract id of the given stock instrument

        :param symbol: Symbol of the stock instrument
        :type symbol: str
        :param instrument_filters: Key-value pair of filters to use on the returned instrument data, e.g) {"name": "ISHARES NATIONAL MUNI BOND E", "assetClass": "STK"}
        :type instrument_filters: dict, optional
        :param contract_filters: Key-value pair of filters to use on the returned contract data, e.g) {"isUS": True, "exchange": "ARCA"}
        :type contract_filters: dict, optional
        :return: contract id
        :rtype: int
        """
        if contract_filters is None:
            contract_filters = {"isUS": True}

        response = await self.client.get(
            f"{self.url}/trsrv/stocks", params={"symbols": symbol}
        )
        instruments_data = response.json()

        if instrument_filters or contract_filters:

            def matches(item: dict, filters: dict) -> bool:
                return all(item.get(k) == v for k, v in filters.items())

            def filter_instrument(instrument: dict) -> bool:
                if instrument_filters and not matches(instrument, instrument_filters):
                    return False
                if contract_filters:
                    instrument["contracts"] = [
                        c
                        for c in instrument["contracts"]
                        if matches(c, contract_filters)
                    ]
                return len(instrument["contracts"]) > 0

            instruments_data[symbol] = list(
                filter(filter_instrument, instruments_data[symbol])
            )

        instrument = StockInstrument(**instruments_data[symbol][0])
        return instrument.contracts[0].conid

    async def get_portfolio(self, account_id=None) -> PortfolioResponse:
        """Returns portfolio of the selected account

        :param account_id: Account ID, uses default if not provided
        :type account_id: str, optional
        :return: Portfolio
        :rtype: PortfolioResponse
        """
        aid = self._require_account_id(account_id)
        response = await self.client.get(f"{self.url}/portfolio/{aid}/positions/0")

        positions = [
            PortfolioPosition(
                contract_desc=item["contractDesc"], position=item["position"]
            )
            for item in response.json()
        ]
        balance = await self.get_cash_balance(account_id=aid)
        return PortfolioResponse(positions=positions, balance=balance)

    async def reply_yes(
        self, message_id: str
    ) -> OrderReplyItem | OrderConfirmationMessage:
        """Replies yes to a single message generated while submitting or modifying orders.

        :param message_id: message ID
        :type message_id: str
        :return: Returned message
        :rtype: OrderReplyItem | OrderConfirmationMessage
        """
        response = await self.client.post(
            f"{self.url}/iserver/reply/{message_id}", json={"confirmed": True}
        )
        data = response.json()
        print(data)
        return self._parse_order_response(data[0])

    def _parse_order_response(
        self, data: dict
    ) -> OrderReplyItem | OrderConfirmationMessage:
        """Parse order response into appropriate model."""
        if "id" in data and "message" in data:
            return OrderConfirmationMessage(**data)
        else:
            return OrderReplyItem(**data)

    async def _reply_all_yes(
        self, response, reply_yes_to_all: bool
    ) -> OrderReplyItem | OrderConfirmationMessage:
        """Replies yes to consecutive messages generated while submitting or modifying orders."""
        result = self._parse_order_response(response.json()[0])
        if reply_yes_to_all:
            while not isinstance(result, OrderReplyItem):
                print("Answering yes to ...")
                if isinstance(result, OrderConfirmationMessage):
                    print(result.message)
                    result = await self.reply_yes(result.id)
                else:
                    break
        return result

    async def submit_orders(
        self, orders: list, account_id=None, reply_yes=True
    ) -> OrderReplyItem | OrderConfirmationMessage:
        """Submit a list of orders

        :param orders: List of order dictionaries. For each order dictionary, see `here <https://www.interactivebrokers.com/api/doc.html#tag/Order/paths/~1iserver~1account~1{accountId}~1orders/post>`_ for more details.
        :type orders: list
        :param account_id: Account ID, uses default if not provided
        :type account_id: str, optional
        :param reply_yes: Replies yes to returning messages or not, defaults to True
        :type reply_yes: bool, optional
        :return: Response to the order request
        :rtype: OrderReplyItem | OrderConfirmationMessage
        """
        aid = self._require_account_id(account_id)
        response = await self.client.post(
            f"{self.url}/iserver/account/{aid}/orders",
            json={"orders": orders},
        )
        if response.status_code != 200:
            raise RuntimeError(
                f"Order submission failed with status {response.status_code}: {response.json()}"
            )

        return await self._reply_all_yes(response, reply_yes)

    async def get_order(self, order_id: str) -> OrderStatus:
        """Returns details of the order

        :param order_id: Order ID of the submitted order
        :type order_id: str
        :return: Details of the order
        :rtype: OrderStatus
        """
        response = await self.client.get(
            f"{self.url}/iserver/account/order/status/{order_id}"
        )
        return OrderStatus(**response.json())

    async def get_live_orders(self, filters=None) -> LiveOrdersResponse:
        """Returns list of live orders

        :param filters: List of filters for the returning response. Available items -- "inactive" "pending_submit" "pre_submitted" "submitted" "filled" "pending_cancel" "cancelled" "warn_state" "sort_by_time", defaults to []
        :type filters: list, optional
        :return: list of live orders
        :rtype: LiveOrdersResponse
        """
        response = await self.client.get(
            f"{self.url}/iserver/account/orders",
            params={"filters": filters or []},
        )
        data = response.json()
        return LiveOrdersResponse(
            orders=[LiveOrder(**item) for item in data.get("orders", [])],
            snapshot=data.get("snapshot", True),
        )

    async def cancel_order(self, order_id: str, account_id=None) -> CancelOrderResponse:
        """Cancel the submitted order

        :param order_id: Order ID for the input order
        :type order_id: str
        :param account_id: Account ID, uses default if not provided
        :type account_id: str, optional
        :return: Response from the server
        :rtype: CancelOrderResponse
        """
        aid = self._require_account_id(account_id)
        response = await self.client.delete(
            f"{self.url}/iserver/account/{aid}/order/{order_id}"
        )
        return CancelOrderResponse(**response.json())

    async def modify_order(
        self, order_id=None, order=None, account_id=None, reply_yes=True
    ) -> OrderReplyItem | OrderConfirmationMessage:
        """Modify submitted order

        :param order_id: Order ID of the submitted order, defaults to None
        :type order_id: str
        :param order: Order dictionary, defaults to None
        :type order: dict
        :param account_id: Account ID, uses default if not provided
        :type account_id: str, optional
        :param reply_yes: Replies yes to the returning messages, defaults to True
        :type reply_yes: bool, optional
        :return: Response from the server
        :rtype: OrderReplyItem | OrderConfirmationMessage
        """
        if order_id is None or order is None:
            raise ValueError("Input parameters (order_id or order) are missing")

        aid = self._require_account_id(account_id)
        response = await self.client.post(
            f"{self.url}/iserver/account/{aid}/order/{order_id}",
            json=order,
        )
        return await self._reply_all_yes(response, reply_yes)

    async def ping_server(self) -> TickleResponse:
        """Tickle server for maintaining connection

        :return: Response from the server
        :rtype: TickleResponse
        """
        response = await self.client.post(f"{self.url}/tickle")
        return TickleResponse(**response.json())

    async def get_auth_status(self) -> AuthStatusResponse:
        """Returns authentication status

        :return: Status dictionary
        :rtype: AuthStatusResponse
        """
        response = await self.client.post(f"{self.url}/iserver/auth/status")
        return AuthStatusResponse(**response.json())

    async def re_authenticate(self) -> ReauthenticateResponse:
        """Attempts to re-authenticate when authentication is lost"""
        response = await self.client.post(f"{self.url}/iserver/reauthenticate")
        print("Reauthenticating ...")
        return ReauthenticateResponse(**response.json())

    async def log_out(self) -> LogoutResponse:
        """Log out from the gateway session"""
        response = await self.client.post(f"{self.url}/logout")
        return LogoutResponse(**response.json())

    async def get_bars(
        self,
        symbol: str,
        period="1w",
        bar="1d",
        outside_rth=False,
        conid: str | int = "default",
    ) -> MarketHistoryResponse:
        """Returns market history for the given instrument. conid should be provided for futures and options.

        :param symbol: Symbol of the stock instrument
        :type symbol: str
        :param period: Period for the history, available time period-- {1-30}min, {1-8}h, {1-1000}d, {1-792}w, {1-182}m, {1-15}y, defaults to "1w"
        :type period: str, optional
        :param bar: Granularity of the history, possible value-- 1min, 2min, 3min, 5min, 10min, 15min, 30min, 1h, 2h, 3h, 4h, 8h, 1d, 1w, 1m, defaults to "1d"
        :type bar: str, optional
        :param outside_rth: For contracts that support it, will determine if historical data includes outside of regular trading hours., defaults to False
        :type outside_rth: bool, optional
        :param conid: conid should be provided separately for futures or options. If not provided, it is assumed to be a stock.
        :type conid: str or int, optional
        :return: Response from the server
        :rtype: MarketHistoryResponse
        """
        if conid == "default":
            conid = await self.get_conid(symbol)

        response = await self.client.get(
            f"{self.url}/iserver/marketdata/history",
            params={
                "conid": int(conid),
                "period": period,
                "bar": bar,
                "outsideRth": outside_rth,
            },
        )
        return MarketHistoryResponse(**response.json())

    async def get_fut_conids(self, symbol: str) -> list[FuturesContract]:
        """Returns list of contract id objects of a future instrument.

        :param symbol: symbol of a future instrument
        :type symbol: str
        :return: list of contract id objects
        :rtype: list[FuturesContract]
        """
        response = await self.client.get(
            f"{self.url}/trsrv/futures", params={"symbols": symbol}
        )
        data = response.json()
        return [FuturesContract(**item) for item in data[symbol]]

    async def get_marketdata_snapshot(
        self,
        symbol: str,
        conid: str | int = "default",
        contract_filters=None,
    ) -> list[MarketDataSnapshot]:
        """Returns market data snapshot for the given instrument. conid should be provided for futures and options.

        :param symbol: Symbol of the stock instrument
        :type symbol: str
        :param conid: conid should be provided separately for futures or options. If not provided, it is assumed to be a stock.
        :type conid: str or int, optional
        :param contract_filters: Key-value pair of filters, defaults to {"isUS": True}
        :type contract_filters: dict, optional
        :return: Response from the server
        :rtype: list[MarketDataSnapshot]
        """
        if contract_filters is None:
            contract_filters = {"isUS": True}
        if conid == "default":
            conid = await self.get_conid(symbol, contract_filters=contract_filters)

        response = await self.client.get(
            f"{self.url}/iserver/marketdata/snapshot",
            params={"conids": conid, "fields": "31"},
        )
        return [MarketDataSnapshot(**item) for item in response.json()]
