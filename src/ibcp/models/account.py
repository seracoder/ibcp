from pydantic import BaseModel, Field


class ParentInfo(BaseModel):
    mmc: list[str] = Field(default_factory=list)
    account_id: str = Field("", alias="accountId")
    is_m_parent: bool = Field(False, alias="isMParent")
    is_m_child: bool = Field(False, alias="isMChild")
    is_multiplex: bool = Field(False, alias="isMultiplex")

    class Config:
        extra = "allow"
        populate_by_name = True


class Account(BaseModel):
    id: str
    account_id: str = Field(..., alias="accountId")
    account_van: str = Field(..., alias="accountVan")
    account_title: str = Field(..., alias="accountTitle")
    display_name: str = Field(..., alias="displayName")
    account_alias: str | None = Field(None, alias="accountAlias")
    account_status: int = Field(..., alias="accountStatus")
    currency: str
    type: str
    trading_type: str = Field(..., alias="tradingType")
    business_type: str = Field(..., alias="businessType")
    ib_entity: str = Field(..., alias="ibEntity")
    faclient: bool = False
    clearing_status: str = Field(..., alias="clearingStatus")
    covestor: bool = False
    no_client_trading: bool = Field(..., alias="noClientTrading")
    track_virtual_fx_portfolio: bool = Field(..., alias="trackVirtualFXPortfolio")
    parent: ParentInfo | None = None
    desc: str
    prepaid_crypto_z: bool = Field(False, alias="PrepaidCrypto-Z")
    prepaid_crypto_p: bool = Field(False, alias="PrepaidCrypto-P")
    brokerage_access: bool = Field(..., alias="brokerageAccess")

    class Config:
        extra = "allow"
        populate_by_name = True


class SwitchAccountResponse(BaseModel):
    success: str | None = None

    class Config:
        extra = "allow"
        populate_by_name = True
