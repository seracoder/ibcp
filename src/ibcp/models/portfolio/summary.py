"""
https://www.interactivebrokers.com/campus/ibkr-api-page/cpapi-v1/#portfolio-summary
Segment suffix meaning
    -s → Securities segment
        Stocks, ETFs, options (equities/derivatives)
        This is usually the main segment for most retail trading accounts
    -c → Commodities segment
        Futures, futures options
        Regulated separately due to different margin rules (CFTC vs SEC)
    -p → Crypto segment (Paxos)
        Crypto balances held via IBKR’s Paxos integration
"""

"""json
{
    accountcode: {
        amount: 0,
        currency: null,
        isNull: false,
        timestamp: 1777616895000,
        value: "DUP340887",
        severity: 0
    },
    accountready: {
        amount: 0,
        currency: null,
        isNull: false,
        timestamp: 1777616895000,
        value: "true",
        severity: 0
    },
    accounttype: {
        amount: 0,
        currency: null,
        isNull: false,
        timestamp: 1777616895000,
        value: "INDIVIDUAL",
        severity: 0
    },
    accruedcash: {
        amount: 2508.22998046875,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    accruedcash-c: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    accruedcash-p: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    accruedcash-s: {
        amount: 2508.22998046875,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    accrueddividend: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    accrueddividend-c: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    accrueddividend-p: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    accrueddividend-s: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    availablefunds: {
        amount: 99575.28125,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    availablefunds-c: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    availablefunds-p: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    availablefunds-s: {
        amount: 99575.28125,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    billable: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    billable-c: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    billable-p: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    billable-s: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    buyingpower: {
        amount: 398301.125,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    columnprio-c: {
        amount: 0,
        currency: null,
        isNull: false,
        timestamp: 1777616895000,
        value: "2",
        severity: 0
    },
    columnprio-p: {
        amount: 0,
        currency: null,
        isNull: false,
        timestamp: 1777616895000,
        value: "5",
        severity: 0
    },
    columnprio-s: {
        amount: 0,
        currency: null,
        isNull: false,
        timestamp: 1777616895000,
        value: "1",
        severity: 0
    },
    cushion: {
        amount: 0,
        currency: null,
        isNull: false,
        timestamp: 1777616895000,
        value: "1",
        severity: 0
    },
    daytradesremaining: {
        amount: 0,
        currency: null,
        isNull: false,
        timestamp: 1777616895000,
        value: "-1",
        severity: 0
    },
    daytradesremainingt+1: {
        amount: 0,
        currency: null,
        isNull: false,
        timestamp: 1777616895000,
        value: "-1",
        severity: 0
    },
    daytradesremainingt+2: {
        amount: 0,
        currency: null,
        isNull: false,
        timestamp: 1777616895000,
        value: "-1",
        severity: 0
    },
    daytradesremainingt+3: {
        amount: 0,
        currency: null,
        isNull: false,
        timestamp: 1777616895000,
        value: "-1",
        severity: 0
    },
    daytradesremainingt+4: {
        amount: 0,
        currency: null,
        isNull: false,
        timestamp: 1777616895000,
        value: "-1",
        severity: 0
    },
    daytradingstatus-s: {
        amount: 0,
        currency: null,
        isNull: false,
        timestamp: 1777616895000,
        value: "::false:99979.59::false",
        severity: 0
    },
    depositoncredithold: {
        amount: 0,
        currency: null,
        isNull: false,
        timestamp: 1777616895000,
        value: "null",
        severity: 0
    },
    equitywithloanvalue: {
        amount: 99979.59375,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    equitywithloanvalue-c: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    equitywithloanvalue-p: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    equitywithloanvalue-s: {
        amount: 99979.59375,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    excessliquidity: {
        amount: 99656.140625,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    excessliquidity-c: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    excessliquidity-p: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    excessliquidity-s: {
        amount: 99656.140625,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    fullavailablefunds: {
        amount: 99575.28125,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    fullavailablefunds-c: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    fullavailablefunds-p: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    fullavailablefunds-s: {
        amount: 99575.28125,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    fullexcessliquidity: {
        amount: 99656.140625,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    fullexcessliquidity-c: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    fullexcessliquidity-p: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    fullexcessliquidity-s: {
        amount: 99656.140625,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    fullinitmarginreq: {
        amount: 404.30999755859375,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    fullinitmarginreq-c: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    fullinitmarginreq-p: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    fullinitmarginreq-s: {
        amount: 404.30999755859375,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    fullmaintmarginreq: {
        amount: 323.45001220703125,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    fullmaintmarginreq-c: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    fullmaintmarginreq-p: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    fullmaintmarginreq-s: {
        amount: 323.45001220703125,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    grosspositionvalue: {
        amount: 4597.08984375,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    grosspositionvalue-s: {
        amount: 4597.08984375,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    guarantee: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    guarantee-c: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    guarantee-p: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    guarantee-s: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    highestseverity: {
        amount: 0,
        currency: null,
        isNull: false,
        timestamp: 1777616895000,
        value: "null",
        severity: 0
    },
    incentivecoupons: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    incentivecoupons-c: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    incentivecoupons-p: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    incentivecoupons-s: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    indianstockhaircut: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    indianstockhaircut-c: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    indianstockhaircut-p: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    indianstockhaircut-s: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    initmarginreq: {
        amount: 404.30999755859375,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    initmarginreq-c: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    initmarginreq-p: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    initmarginreq-s: {
        amount: 404.30999755859375,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    leverage-s: {
        amount: 0,
        currency: null,
        isNull: false,
        timestamp: 1777616895000,
        value: "0.04",
        severity: 0
    },
    lookaheadavailablefunds: {
        amount: 99575.28125,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    lookaheadavailablefunds-c: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    lookaheadavailablefunds-p: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    lookaheadavailablefunds-s: {
        amount: 99575.28125,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    lookaheadexcessliquidity: {
        amount: 99656.140625,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    lookaheadexcessliquidity-c: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    lookaheadexcessliquidity-p: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    lookaheadexcessliquidity-s: {
        amount: 99656.140625,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    lookaheadinitmarginreq: {
        amount: 404.30999755859375,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    lookaheadinitmarginreq-c: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    lookaheadinitmarginreq-p: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    lookaheadinitmarginreq-s: {
        amount: 404.30999755859375,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    lookaheadmaintmarginreq: {
        amount: 323.45001220703125,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    lookaheadmaintmarginreq-c: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    lookaheadmaintmarginreq-p: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    lookaheadmaintmarginreq-s: {
        amount: 323.45001220703125,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    lookaheadnextchange: {
        amount: 0,
        currency: null,
        isNull: false,
        timestamp: 1777616895000,
        value: "0",
        severity: 0
    },
    maintmarginreq: {
        amount: 323.45001220703125,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    maintmarginreq-c: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    maintmarginreq-p: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    maintmarginreq-s: {
        amount: 323.45001220703125,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    netliquidation: {
        amount: 102487.8203125,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    netliquidation-c: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    netliquidation-p: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    netliquidation-s: {
        amount: 102487.8203125,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    netliquidationuncertainty: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    nlvandmargininreview: {
        amount: 0,
        currency: null,
        isNull: false,
        timestamp: 1777616895000,
        value: "false",
        severity: 0
    },
    pasharesvalue: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    pasharesvalue-c: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    pasharesvalue-p: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    pasharesvalue-s: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    physicalcertificatevalue: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    physicalcertificatevalue-c: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    physicalcertificatevalue-p: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    physicalcertificatevalue-s: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    postexpirationexcess: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    postexpirationexcess-c: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    postexpirationexcess-p: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    postexpirationexcess-s: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    postexpirationmargin: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    postexpirationmargin-c: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    postexpirationmargin-p: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    postexpirationmargin-s: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    previousdayequitywithloanvalue: {
        amount: 100000,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    previousdayequitywithloanvalue-s: {
        amount: 100000,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    regtequity: {
        amount: 102487.8203125,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    regtequity-s: {
        amount: 102487.8203125,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    regtmargin: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    regtmargin-s: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    segmenttitle-c: {
        amount: 0,
        currency: null,
        isNull: false,
        timestamp: 1777616895000,
        value: "US Commodities",
        severity: 0
    },
    segmenttitle-p: {
        amount: 0,
        currency: null,
        isNull: false,
        timestamp: 1777616895000,
        value: "Crypto at Paxos",
        severity: 0
    },
    segmenttitle-s: {
        amount: 0,
        currency: null,
        isNull: false,
        timestamp: 1777616895000,
        value: "US Securities",
        severity: 0
    },
    settledcashbydate: {
        amount: 0,
        currency: null,
        isNull: false,
        timestamp: 1777616895000,
        value: "20260501:99998;20260505:95382.5",
        severity: 0
    },
    settledcashbydate-c: {
        amount: 0,
        currency: null,
        isNull: false,
        timestamp: 1777616895000,
        value: "20260501:0",
        severity: 0
    },
    settledcashbydate-p: {
        amount: 0,
        currency: null,
        isNull: false,
        timestamp: 1777616895000,
        value: "20260501:0",
        severity: 0
    },
    settledcashbydate-s: {
        amount: 0,
        currency: null,
        isNull: false,
        timestamp: 1777616895000,
        value: "20260501:99998;20260505:95382.5",
        severity: 0
    },
    sma: {
        amount: 102487.8203125,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    sma-s: {
        amount: 102487.8203125,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    totalcashvalue: {
        amount: 95382.5,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    totalcashvalue-c: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    totalcashvalue-p: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    totalcashvalue-s: {
        amount: 95382.5,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    totaldebitcardpendingcharges: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    totaldebitcardpendingcharges-c: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    totaldebitcardpendingcharges-p: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    totaldebitcardpendingcharges-s: {
        amount: 0,
        currency: "USD",
        isNull: false,
        timestamp: 1777616895000,
        value: null,
        severity: 0
    },
    tradingtype-s: {
        amount: 0,
        currency: null,
        isNull: false,
        timestamp: 1777616895000,
        value: "STKNOPT",
        severity: 0
    },
    whatifpmenabled: {
        amount: 0,
        currency: null,
        isNull: false,
        timestamp: 1777616895000,
        value: "true",
        severity: 0
    }
}"""

from typing import Literal, Optional, Union
from pydantic import BaseModel, field_validator

SummaryKeys = Literal[
    # Identity / metadata
    "accountcode",
    "accounttype",
    "accountready",

    # Core portfolio value
    "netliquidation",          # total account value (MOST IMPORTANT)
    "equitywithloanvalue",     # margin-aware equity
    "previousdayequitywithloanvalue",

    # Cash & balances
    "totalcashvalue",
    "settledcash",
    "accruedcash",
    "accrueddividend",

     # Buying power / capital
    "buyingpower",
    "availablefunds",
    "excessliquidity",
    "cushion",

    # Margin requirements
    "initmarginreq",
    "maintmarginreq",

     # Positions exposure
    "grosspositionvalue",

    # Reg-T / SMA (important for US margin accounts)
    "sma",
    "regtequity",
    "regtmargin",

    # Risk / status
    "daytradingstatus",
    "daytradesremaining",
    "leverage",

    # Lookahead (useful for projections)
    "lookaheadavailablefunds",
    "lookaheadexcessliquidity",
    "lookaheadinitmarginreq",
    "lookaheadmaintmarginreq",
]

class SummarySuffixed(BaseModel):
    total: float
    securities: Optional[float] = None
    commodities: Optional[float] = None
    crypto: Optional[float] = None

class Summary(BaseModel):
    # --- Identity ---
    account_code: str
    account_type: str
    is_account_ready: bool

    # --- Core portfolio ---
    net_liquidation: SummarySuffixed
    equity_with_loan_value: SummarySuffixed
    previous_day_equity_with_loan_value: SummarySuffixed

    # --- Cash ---
    total_cash_value: SummarySuffixed
    accrued_cash: SummarySuffixed
    accrued_dividend: SummarySuffixed

    # --- Buying power / capital ---
    buying_power: SummarySuffixed
    available_funds: SummarySuffixed
    excess_liquidity: SummarySuffixed
    cushion: Optional[float]  # this comes from `value`, not amount

    # --- Margin ---
    initial_margin_requirement: SummarySuffixed
    maintenance_margin_requirement: SummarySuffixed

    # --- Exposure ---
    gross_position_value: SummarySuffixed

    # --- Reg-T ---
    sma: SummarySuffixed
    regt_equity: SummarySuffixed
    regt_margin: SummarySuffixed

    # --- Risk / status ---
    day_trades_remaining: Optional[int]
    leverage: Optional[float]

    # --- Lookahead ---
    lookahead_available_funds: SummarySuffixed
    lookahead_excess_liquidity: SummarySuffixed
    lookahead_initial_margin_requirement: SummarySuffixed
    lookahead_maintenance_margin_requirement: SummarySuffixed