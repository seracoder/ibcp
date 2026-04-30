from pydantic import BaseModel, Field


class StockContract(BaseModel):
    conid: int
    exchange: str
    is_us: bool = Field(..., alias="isUS")

    class Config:
        extra = "allow"
        populate_by_name = True


class StockInstrument(BaseModel):
    name: str
    chinese_name: str = Field("", alias="chineseName")
    asset_class: str = Field(..., alias="assetClass")
    contracts: list[StockContract]

    class Config:
        extra = "allow"
        populate_by_name = True


class FuturesContract(BaseModel):
    symbol: str
    conid: int
    underlying_conid: int = Field(..., alias="underlyingConid")
    expiration_date: int = Field(..., alias="expirationDate")
    ltd: int
    short_futures_cut_off: int = Field(..., alias="shortFuturesCutOff")
    long_futures_cut_off: int = Field(..., alias="longFuturesCutOff")

    class Config:
        extra = "allow"
        populate_by_name = True
