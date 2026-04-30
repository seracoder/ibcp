from pydantic import BaseModel, Field


class MarketDataSnapshot(BaseModel):
    updated: int = Field(..., alias="_updated")
    conid_ex: str = Field(..., alias="conidEx")
    conid: int
    server_id: str = Field(..., alias="server_id")

    class Config:
        extra = "allow"
        populate_by_name = True


class Bar(BaseModel):
    o: float
    c: float
    h: float
    l: float
    v: float
    t: int

    class Config:
        extra = "allow"
        populate_by_name = True


class MarketHistoryResponse(BaseModel):
    server_id: str = Field(..., alias="serverId")
    symbol: str
    text: str
    price_factor: int | str = Field(..., alias="priceFactor")
    start_time: str = Field(..., alias="startTime")
    high: str
    low: str
    time_period: str = Field(..., alias="timePeriod")
    bar_length: int = Field(..., alias="barLength")
    md_availability: str = Field(..., alias="mdAvailability")
    mkt_data_delay: int = Field(0, alias="mktDataDelay")
    outside_rth: bool = Field(..., alias="outsideRth")
    trading_day_duration: int | None = Field(None, alias="tradingDayDuration")
    volume_factor: int = Field(1, alias="volumeFactor")
    price_display_rule: int | None = Field(None, alias="priceDisplayRule")
    price_display_value: str | None = Field(None, alias="priceDisplayValue")
    chart_pan_start_time: str | None = Field(None, alias="chartPanStartTime")
    direction: int = 0
    negative_capable: bool = Field(..., alias="negativeCapable")
    message_version: int = Field(2, alias="messageVersion")
    data: list[Bar] = Field(default_factory=list)
    points: int = 0
    travel_time: int = Field(..., alias="travelTime")

    class Config:
        extra = "allow"
        populate_by_name = True
