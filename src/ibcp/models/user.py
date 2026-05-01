from pydantic import BaseModel

class Feature(BaseModel):
    env: str
    wlms: bool
    realtime: bool
    bond: bool
    optionChains: bool
    calendar: bool
    newMf: bool


class UAR(BaseModel):
    portfolioAnalyst: bool
    userInfo: bool
    messageCenter: bool
    accountDetails: bool
    tradingRestrictions: bool
    tws: bool
    fyi: bool
    voting: bool
    forum: bool
    recentTransactions: bool


class Props(BaseModel):
    isIBAMClient: bool
    ReadOnlySession: str | None

class ACCTS(BaseModel):
    isIBAMClient: bool
    clearingStatus: str
    openDate: int
    isFAClient: bool
    isFunded: bool
    tradingPermissions: list[str]


class APPLICANT(BaseModel):
    id: int
    type: str
    businessType: str
    nlcode: str
    legalCountry: dict


class User(BaseModel):
    username: str
    features: Feature
    wbId: str
    uar: UAR
    props: Props
    accts: dict[str, ACCTS]
    hasBrokerageAccessInd: bool
    hfcipEligibleInd: bool
    fa: bool
    has2fa: bool
    islite: bool
    ispaper: bool
    applicants: list[APPLICANT]
