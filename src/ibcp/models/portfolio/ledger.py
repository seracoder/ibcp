"""
{
    USD: {
        commoditymarketvalue: 4578.2,
        futuremarketvalue: 0,
        settledcash: 94595.46,
        exchangerate: 1,
        sessionid: 1,
        cashbalance: 94595.46,
        corporatebondsmarketvalue: 0,
        warrantsmarketvalue: 0,
        netliquidationvalue: 102640.34,
        interest: 2618.3,
        unrealizedpnl: 22.04,
        stockmarketvalue: 848.38,
        moneyfunds: 0,
        currency: "USD",
        realizedpnl: 0,
        funds: 0,
        acctcode: "DUP340887",
        issueroptionsmarketvalue: 0,
        key: "LedgerList",
        timestamp: 1777992005,
        severity: 0,
        stockoptionmarketvalue: 0,
        futuresonlypnl: 0,
        tbondsmarketvalue: 0,
        futureoptionmarketvalue: 0,
        cashbalancefxsegment: 0,
        secondkey: "USD",
        tbillsmarketvalue: 0,
        endofbundle: 1,
        dividends: 0,
        cryptocurrencyvalue: 0
    },
    BASE: {
        commoditymarketvalue: 4578.2,
        futuremarketvalue: 0,
        settledcash: 94595.46,
        exchangerate: 1,
        sessionid: 1,
        cashbalance: 94595.46,
        corporatebondsmarketvalue: 0,
        warrantsmarketvalue: 0,
        netliquidationvalue: 102640.34,
        interest: 2618.3,
        unrealizedpnl: 22.04,
        stockmarketvalue: 848.38,
        moneyfunds: 0,
        currency: "BASE",
        realizedpnl: 0,
        funds: 0,
        acctcode: "DUP340887",
        issueroptionsmarketvalue: 0,
        key: "LedgerList",
        timestamp: 1777992005,
        severity: 0,
        stockoptionmarketvalue: 0,
        futuresonlypnl: 0,
        tbondsmarketvalue: 0,
        futureoptionmarketvalue: 0,
        cashbalancefxsegment: 0,
        secondkey: "BASE",
        tbillsmarketvalue: 0,
        dividends: 0,
        cryptocurrencyvalue: 0
    }
}

"""
from pydantic import BaseModel, Field

class Ledger(BaseModel):
    commodity_market_value: float = Field(0.0, alias="commoditymarketvalue")
    future_market_value: float = Field(0.0, alias="futuremarketvalue")
    settled_cash: float = Field(0.0, alias="settledcash")
    exchange_rate: float = Field(0.0, alias="exchangerate")
    session_id: int = Field(0, alias="sessionid")
    cash_balance: float = Field(0.0, alias="cashbalance")
    corporate_bonds_market_value: float = Field(0.0, alias="corporatebondsmarketvalue")
    warrants_market_value: float = Field(0.0, alias="warrantsmarketvalue")
    net_liquidation_value: float = Field(0.0, alias="netliquidationvalue")
    interest: float = Field(0.0, alias="interest")
    unrealized_pnl: float = Field(0.0, alias="unrealizedpnl")
    stock_market_value: float = Field(0.0, alias="stockmarketvalue")
    money_funds: float = Field(0.0, alias="moneyfunds")
    currency: str
    realized_pnl: float = Field(0.0, alias="realizedpnl")
    funds: float = Field(0.0, alias="funds")
    acct_code: str = Field("", alias="acctcode")
    issuer_options_market_value: float = Field(0.0, alias="issueroptionsmarketvalue")
    key: str = Field("", alias="key")
    timestamp: int = Field(0, alias="timestamp")
    severity: int = Field(0, alias="severity")
    stock_option_market_value: float = Field(0.0, alias="stockoptionmarketvalue")
    futures_only_pnl: float = Field(0.0, alias="futuresonlypnl")
    t_bonds_market_value: float = Field(0.0, alias="tbondsmarketvalue")
    future_option_market_value: float = Field(0.0, alias="futureoptionmarketvalue")
    cash_balance_fx_segment: float = Field(0.0, alias="cashbalancefxsegment")
    second_key: str = Field("", alias="secondkey")
    t_bills_market_value: float = Field(0.0, alias="tbillsmarketvalue")
    end_of_bundle: int = Field(0, alias="endofbundle")
    dividends: float = Field(0.0, alias="dividends")
    cryptocurrency_value: float = Field(0.0, alias="cryptocurrencyvalue")