from typing import Optional

from pydantic import BaseModel, Field


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

    class Config:
        extra = "allow"
        populate_by_name = True


class DisplayRuleStep(BaseModel):
    decimal_digits: int = 0
    lower_edge: float = 0.0
    whole_digits: int = 0

    class Config:
        extra = "allow"
        populate_by_name = True


class DisplayRule(BaseModel):
    magnification: int = 0
    display_rule_step: list[DisplayRuleStep] = Field(default_factory=list)

    class Config:
        extra = "allow"
        populate_by_name = True


class Position(BaseModel):
    # https://www.interactivebrokers.com/campus/ibkr-api-page/cpapi-v1/#positions
    acct_id: str = Field(..., alias="acctId")
    con_id: int = Field(..., alias="conid")
    contract_desc: str = Field(..., alias="contractDesc")
    position: float
    mkt_price: float = Field(0.0, alias="mktPrice")
    mkt_value: float = Field(0.0, alias="mktValue")
    currency: str
    avg_cost: float = Field(0.0, alias="avgCost")
    avg_price: float = Field(0.0, alias="avgPrice")
    realized_pnl: float = Field(0.0, alias="realizedPnl")
    unrealized_pnl: float = Field(0.0, alias="unrealizedPnl")
    exchs: Optional[str]
    chinese_name: str = Field("", alias="chineseName")
    all_exchanges: str = Field("", alias="allExchanges")
    listing_exchange: str = Field("", alias="listingExchange")
    country_code: str = Field("", alias="countryCode")
    name: str
    asset_class: str = Field("", alias="assetClass")
    expiry: str | None = None
    last_trading_day: str = Field("", alias="lastTradingDay")
    group: str = Field("")
    put_or_call: str | None = Field(None, alias="putOrCall")
    sector: str = Field("")
    sector_group: str = Field("", alias="sectorGroup")
    strike: float = 0.0
    ticker: str
    und_conid: int = Field(0, alias="undConid")
    model: str = Field("")
    increment_rules: list[IncrementRule] = Field(
        default_factory=list, alias="incrementRules"
    )
    display_rule: DisplayRule | None = Field(None, alias="displayRule")
    time: int = Field(0)
    multiplier: float | None = None
    type: str = Field("")
    has_options: bool = Field(False, alias="hasOptions")
    full_name: str = Field("", alias="fullName")
    is_us: bool = Field(False, alias="isUS")
    exercise_style: str | None = Field(None, alias="exerciseStyle")
    con_exch_map: list = Field(default_factory=list, alias="conExchMap")
    is_event_contract: bool = Field(False, alias="isEventContract")
    page_size: int = Field(0, alias="pageSize")

    class Config:
        extra = "allow"
        populate_by_name = True
