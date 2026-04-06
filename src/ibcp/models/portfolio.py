from pydantic import BaseModel, Field


class LedgerEntry(BaseModel):
    commoditymarketvalue: float = 0.0
    futuremarketvalue: float = 0.0
    settledcash: float = 0.0
    exchangerate: int = 1
    sessionid: int = 0
    cashbalance: float = 0.0
    corporatebondsmarketvalue: float = 0.0
    warrantsmarketvalue: float = 0.0
    netliquidationvalue: float = 0.0
    interest: float = 0.0
    unrealizedpnl: float = 0.0
    stockmarketvalue: float = 0.0
    moneyfunds: float = 0.0
    currency: str
    realizedpnl: float = 0.0
    funds: float = 0.0
    acctcode: str
    issueroptionsmarketvalue: float = 0.0
    key: str = "LedgerList"
    timestamp: int = 0
    severity: int = 0
    stockoptionmarketvalue: float = 0.0
    futuresonlypnl: float = 0.0
    tbondsmarketvalue: float = 0.0
    futureoptionmarketvalue: float = 0.0
    cashbalancefxsegment: float = 0.0
    secondkey: str
    tbillsmarketvalue: float = 0.0
    endofbundle: int = 0
    dividends: float = 0.0

    model_config = {"extra": "allow", "populate_by_name": True}


class CurrencyValue(BaseModel):
    currency: str
    value: float


class CashBalanceResponse(BaseModel):
    items: list[CurrencyValue]


class NetValueResponse(BaseModel):
    items: list[CurrencyValue]


class IncrementRule(BaseModel):
    lower_edge: float = 0.0
    increment: float = 0.0

    model_config = {"extra": "allow", "populate_by_name": True}


class DisplayRuleStep(BaseModel):
    decimal_digits: int = 0
    lower_edge: float = 0.0
    whole_digits: int = 0

    model_config = {"extra": "allow", "populate_by_name": True}


class DisplayRule(BaseModel):
    magnification: int = 0
    display_rule_step: list[DisplayRuleStep] = Field(default_factory=list)

    model_config = {"extra": "allow", "populate_by_name": True}


class Position(BaseModel):
    acct_id: str = Field(..., alias="acctId")
    conid: int
    contract_desc: str = Field(..., alias="contractDesc")
    position: float
    mkt_price: float = Field(0.0, alias="mktPrice")
    mkt_value: float = Field(0.0, alias="mktValue")
    currency: str
    avg_cost: float = Field(0.0, alias="avgCost")
    avg_price: float = Field(0.0, alias="avgPrice")
    realized_pnl: float = Field(0.0, alias="realizedPnl")
    unrealized_pnl: float = Field(0.0, alias="unrealizedPnl")
    exchs: None = None
    time: int = 0
    chinese_name: str = Field("", alias="chineseName")
    all_exchanges: str = Field("", alias="allExchanges")
    listing_exchange: str = Field("", alias="listingExchange")
    country_code: str = Field("", alias="countryCode")
    name: str
    asset_class: str = Field("", alias="assetClass")
    expiry: str | None = None
    last_trading_day: str = Field("", alias="lastTradingDay")
    group: str = ""
    put_or_call: str | None = Field(None, alias="putOrCall")
    sector: str = ""
    sector_group: str = Field("", alias="sectorGroup")
    strike: float = 0.0
    ticker: str
    und_conid: int = Field(0, alias="undConid")
    multiplier: float | None = None
    type: str = ""
    has_options: bool = Field(False, alias="hasOptions")
    full_name: str = Field("", alias="fullName")
    is_us: bool = Field(False, alias="isUS")
    exercise_style: str | None = Field(None, alias="exerciseStyle")
    con_exch_map: list = Field(default_factory=list, alias="conExchMap")
    model: str = ""
    is_event_contract: bool = Field(False, alias="isEventContract")
    page_size: int = Field(0, alias="pageSize")
    increment_rules: list[IncrementRule] = Field(
        default_factory=list, alias="incrementRules"
    )
    display_rule: DisplayRule | None = Field(None, alias="displayRule")

    model_config = {"extra": "allow", "populate_by_name": True}


class PortfolioPosition(BaseModel):
    contract_desc: str
    position: float


class PortfolioResponse(BaseModel):
    positions: list[PortfolioPosition]
    balance: CashBalanceResponse
