from pydantic import BaseModel, Field


class OrderConfirmationMessage(BaseModel):
    id: str
    message: list[str]
    is_suppressed: bool = Field(False, alias="isSuppressed")
    message_ids: list[str] = Field(default_factory=list, alias="messageIds")

    model_config = {"extra": "allow", "populate_by_name": True}


class OrderReplyItem(BaseModel):
    order_id: str = Field(..., alias="order_id")
    order_status: str = Field(..., alias="order_status")
    encrypt_message: str = Field("", alias="encrypt_message")

    model_config = {"extra": "allow", "populate_by_name": True}


OrderReply = list[OrderConfirmationMessage | OrderReplyItem]


class OrderStatus(BaseModel):
    sub_type: None = None
    request_id: str = Field(..., alias="request_id")
    server_id: str = Field(..., alias="server_id")
    order_id: int = Field(..., alias="order_id")
    conidex: str = Field(..., alias="conidex")
    conid: int
    symbol: str
    side: str
    contract_description_1: str = Field(..., alias="contract_description_1")
    listing_exchange: str = Field(..., alias="listing_exchange")
    option_acct: str = Field(..., alias="option_acct")
    company_name: str = Field(..., alias="company_name")
    size: str
    total_size: str = Field(..., alias="total_size")
    currency: str
    account: str
    order_type: str = Field(..., alias="order_type")
    cum_fill: str = Field(..., alias="cum_fill")
    order_status: str = Field(..., alias="order_status")
    order_ccp_status: str = Field(..., alias="order_ccp_status")
    order_status_description: str = Field(..., alias="order_status_description")
    tif: str
    fg_color: str = Field(..., alias="fg_color")
    bg_color: str = Field(..., alias="bg_color")
    order_not_editable: bool = Field(..., alias="order_not_editable")
    editable_fields: str = Field(..., alias="editable_fields")
    cannot_cancel_order: bool = Field(..., alias="cannot_cancel_order")
    deactivate_order: bool = Field(..., alias="deactivate_order")
    sec_type: str = Field(..., alias="sec_type")
    available_chart_periods: str = Field(..., alias="available_chart_periods")
    order_description: str = Field(..., alias="order_description")
    order_description_with_contract: str = Field(
        ..., alias="order_description_with_contract"
    )
    alert_active: int = 1
    child_order_type: str = Field(..., alias="child_order_type")
    order_clearing_account: str = Field(..., alias="order_clearing_account")
    size_and_fills: str = Field(..., alias="size_and_fills")
    exit_strategy_display_price: str = Field(..., alias="exit_strategy_display_price")
    exit_strategy_chart_description: str = Field(
        ..., alias="exit_strategy_chart_description"
    )
    average_price: str = Field(..., alias="average_price")
    exit_strategy_tool_availability: str = Field(
        ..., alias="exit_strategy_tool_availability"
    )
    allowed_duplicate_opposite: bool = Field(..., alias="allowed_duplicate_opposite")
    order_time: str = Field(..., alias="order_time")

    model_config = {"extra": "allow", "populate_by_name": True}


class LiveOrder(BaseModel):
    acct: str
    conidex: str
    conid: int
    account: str
    order_id: int = Field(..., alias="orderId")
    cash_ccy: str = Field(..., alias="cashCcy")
    size_and_fills: str = Field(..., alias="sizeAndFills")
    order_desc: str = Field(..., alias="orderDesc")
    description1: str = Field(..., alias="description1")
    ticker: str
    sec_type: str = Field(..., alias="secType")
    listing_exchange: str = Field(..., alias="listingExchange")
    remaining_quantity: float = 0.0
    filled_quantity: float = 0.0
    total_size: float = 0.0
    company_name: str = Field(..., alias="companyName")
    status: str
    order_ccp_status: str = Field(..., alias="order_ccp_status")
    avg_price: str = Field(..., alias="avgPrice")
    orig_order_type: str = Field(..., alias="origOrderType")
    supports_tax_opt: str = Field(..., alias="supportsTaxOpt")
    last_execution_time: str = Field(..., alias="lastExecutionTime")
    order_type: str = Field(..., alias="orderType")
    bg_color: str = Field(..., alias="bgColor")
    fg_color: str = Field(..., alias="fgColor")
    order_ref: str = Field(..., alias="order_ref")
    time_in_force: str = Field(..., alias="timeInForce")
    last_execution_time_r: int = Field(..., alias="lastExecutionTime_r")
    side: str

    model_config = {"extra": "allow", "populate_by_name": True}


class LiveOrdersResponse(BaseModel):
    orders: list[LiveOrder]
    snapshot: bool = True


class CancelOrderResponse(BaseModel):
    msg: str
    order_id: int = Field(..., alias="order_id")
    conid: int
    account: str | None = None

    model_config = {"extra": "allow", "populate_by_name": True}
