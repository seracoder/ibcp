"""
{
username: "kbshyv347",
features: {
env: "PROD",
wlms: true,
realtime: true,
bond: true,
optionChains: true,
calendar: true,
newMf: true
},
wbId: "",
uar: {
portfolioAnalyst: true,
userInfo: true,
messageCenter: true,
accountDetails: true,
tradingRestrictions: true,
tws: true,
fyi: true,
voting: true,
forum: true,
recentTransactions: true
},
props: {
isIBAMClient: false,
ReadOnlySession: null
},
accts: {
DUP340887: {
isIBAMClient: false,
clearingStatus: "O",
openDate: 1772812800000,
isFAClient: false,
isFunded: true,
tradingPermissions: [
"CFD",
"CRYPTO",
"WGR",
"FUT",
"FUND",
"IOPT",
"WAR",
"STK",
"CMDTY",
"CASH",
"OPT",
"BILL",
"BOND",
"FOP",
"SSF"
]
}
},
hasBrokerageAccessInd: true,
hfcipEligibleInd: false,
fa: false,
has2fa: false,
islite: false,
ispaper: true,
applicants: [
{
id: 24202783,
type: "INDIVIDUAL",
businessType: "INDEPENDENT",
nlcode: "en_US",
legalCountry: {
name: "Bangladesh",
alpha3: "BGD"
}
}
]
}

"""


from pydantic import BaseModel, Field

class Feature(BaseModel):
    env: str
    wlms: bool
    realtime: bool
    bond: bool
    optionChains: bool
    calendar: bool
    newMF: bool


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


__ALL__ = ["User"]