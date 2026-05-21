from typing import Optional

from pydantic import BaseModel, Field, AliasChoices


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


class PositionBase(BaseModel):
    position: int = Field(..., alias="position")
    con_id: int = Field(..., alias="conid")
    avg_cost: float = Field(0.0, alias="avgCost")
    avg_price: float = Field(0.0, alias="avgPrice")
    currency: str
    mkt_price: float = Field(0.0, validation_alias=AliasChoices("mktPrice", "marketPrice"))
    mkt_value: float = Field(0.0, validation_alias=AliasChoices("mktValue", "marketValue"))
    realized_pnl: float = Field(0.0, alias="realizedPnl")
    unrealized_pnl: float = Field(0.0, alias="unrealizedPnl")
    asset_class: str = Field("", alias="assetClass")
    sector: str = Field("")
    group: str = Field("")
    und_conid: int = Field(0, alias="undConid")

    class Config:
        extra = "allow"
        populate_by_name = True


class Position(PositionBase):
    # https://www.interactivebrokers.com/campus/ibkr-api-page/cpapi-v1/#positions
    acct_id: str = Field(..., alias="acctId")
    contract_desc: str = Field(..., alias="contractDesc")
    exchs: Optional[str]
    chinese_name: str = Field("", alias="chineseName")
    all_exchanges: str = Field("", alias="allExchanges")
    listing_exchange: str = Field("", alias="listingExchange")
    country_code: str = Field("", alias="countryCode")
    name: str
    expiry: str | None = None
    last_trading_day: str = Field("", alias="lastTradingDay")
    put_or_call: str | None = Field(None, alias="putOrCall")
    sector_group: str = Field("", alias="sectorGroup")
    strike: float = 0.0
    ticker: str
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


class Position2(PositionBase):
    description: str = Field(description="Position Symbol")
    sec_type: str = Field("", alias="secType")
    is_last_to_loq: bool = Field(False, alias="isLastToLoq")
    timestamp: int
