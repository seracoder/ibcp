import pytest
import pytest_asyncio

from ibcp import REST


@pytest_asyncio.fixture
async def api():
    client = REST(url="http://localhost:5000")
    yield client
    await client.close()


@pytest_asyncio.fixture
async def account_id(api):
    accounts = await api.get_accounts()
    assert accounts, "No accounts found"
    aid = accounts[0].account_id
    await api.set_default_account()
    return aid


@pytest.mark.asyncio
async def test_ping_server(api):
    result = await api.ping_server()
    assert result.session


@pytest.mark.asyncio
async def test_get_auth_status(api):
    result = await api.get_auth_status()
    assert result.authenticated

@pytest.mark.asyncio
async def test_get_user(api):
    result = await api.get_user()
    assert result.username != ""


@pytest.mark.asyncio
async def test_get_accounts(api):
    accounts = await api.get_accounts()
    assert len(accounts) > 0


@pytest.mark.asyncio
async def test_switch_account(api, account_id):
    result = await api.switch_account(account_id)
    assert result.success is not None


@pytest.mark.asyncio
async def test_get_cash_balance(api, account_id):
    result = await api.get_cash_balance()
    assert len(result.items) > 0


@pytest.mark.asyncio
async def test_get_cash_balance_usd(api, account_id):
    result = await api.get_cash_balance(currency="USD")
    assert len(result.items) > 0


@pytest.mark.asyncio
async def test_get_netvalue(api, account_id):
    result = await api.get_netvalue()
    assert len(result.items) > 0


@pytest.mark.asyncio
async def test_get_netvalue_usd(api, account_id):
    result = await api.get_netvalue(currency="USD")
    assert len(result.items) > 0


@pytest.mark.asyncio
async def test_get_portfolio(api, account_id):
    result = await api.get_portfolio()
    assert result.balance is not None


@pytest.mark.asyncio
async def test_get_conid(api):
    conid = await api.get_conid("AAPL")
    assert isinstance(conid, int)


@pytest.mark.asyncio
async def test_get_marketdata_snapshot(api):
    result = await api.get_marketdata_snapshot("AAPL")
    assert len(result) > 0


@pytest.mark.asyncio
async def test_get_stock_last_price(api):
    price = await api.get_stock_last_price("AAPL")
    assert isinstance(price, float)
    assert price > 0


@pytest.mark.asyncio
async def test_get_bars(api):
    result = await api.get_bars("AAPL")
    assert result.symbol == "AAPL"


@pytest.mark.asyncio
async def test_get_fut_conids(api):
    result = await api.get_fut_conids("ES")
    assert len(result) > 0


@pytest.mark.asyncio
async def test_submit_and_cancel_order(api, account_id):
    aapl_conid = await api.get_conid("AAPL")
    orders = [
        {
            "conid": aapl_conid,
            "orderType": "LMT",
            "side": "BUY",
            "quantity": 1,
            "tif": "GTC",
            "price": 1,
        }
    ]
    await api.submit_orders(orders)

    live = await api.get_live_orders()
    assert len(live.orders) > 0

    order_id = str(live.orders[0].order_id)
    status = await api.get_order(order_id)
    assert status.order_id > 0

    result = await api.cancel_order(order_id)
    assert result.msg


@pytest.mark.asyncio
async def test_re_authenticate(api):
    result = await api.re_authenticate()
    assert result.message
