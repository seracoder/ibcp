from pydantic import BaseModel, Field


class MarketDataSnapshot(BaseModel):
    updated: int = Field(..., alias="_updated")
    conid_ex: str = Field(..., alias="conidEx")
    conid: int
    server_id: str = Field(..., alias="server_id")

    model_config = {"extra": "allow", "populate_by_name": True}


class Bar(BaseModel):
    o: float
    c: float
    h: float
    low: float
    v: float
    t: int


class MarketHistoryResponse(BaseModel):
    server_id: str = Field(..., alias="serverId")
    symbol: str
    text: str
    price_factor: str = Field(..., alias="priceFactor")
    start_time: str = Field(..., alias="startTime")
    high: str
    low: str
    time_period: str = Field(..., alias="timePeriod")
    bar_length: int = Field(..., alias="barLength")
    md_availability: str = Field(..., alias="mdAvailability")
    mkt_data_delay: int = Field(0, alias="mktDataDelay")
    outside_rth: bool = Field(..., alias="outsideRth")
    trading_day_duration: int = Field(..., alias="tradingDayDuration")
    volume_factor: int = Field(1, alias="volumeFactor")
    price_display_rule: int = Field(..., alias="priceDisplayRule")
    price_display_value: str = Field("", alias="priceDisplayValue")
    chart_pan_start_time: str = Field("", alias="chartPanStartTime")
    direction: int = 0
    negative_capable: bool = Field(..., alias="negativeCapable")
    message_version: int = Field(2, alias="messageVersion")
    data: list[Bar]
    points: int = 0
    travel_time: int = Field(..., alias="travelTime")

    model_config = {"extra": "allow", "populate_by_name": True}
