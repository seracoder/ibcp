from pydantic import BaseModel, Field


class OrderConfirmationMessage(BaseModel):
    id: str
    message: list[str]
    is_suppressed: bool = Field(False, alias="isSuppressed")
    message_ids: list[str] = Field(default_factory=list, alias="messageIds")

    class Config:
        extra = "allow"
        populate_by_name = True


class OrderReplyItem(BaseModel):
    order_id: str = Field(..., alias="order_id")
    order_status: str = Field(..., alias="order_status")
    encrypt_message: str = Field("", alias="encrypt_message")

    class Config:
        extra = "allow"
        populate_by_name = True


OrderReply = list[OrderConfirmationMessage | OrderReplyItem]


class OrderStatus(BaseModel):
    sub_type: str | None = None
    request_id: str = ""
    server_id: str = ""
    order_id: int = 0
    conidex: str = ""
    conid: int = 0
    symbol: str = ""
    side: str = ""
    contract_description_1: str = ""
    listing_exchange: str = ""
    option_acct: str = ""
    company_name: str = ""
    size: str = ""
    total_size: str = ""
    currency: str = ""
    account: str = ""
    order_type: str = ""
    cum_fill: str = ""
    order_status: str = ""
    order_ccp_status: str = ""
    order_status_description: str = ""
    tif: str = ""
    fg_color: str = ""
    bg_color: str = ""
    order_not_editable: bool = False
    editable_fields: str = ""
    cannot_cancel_order: bool = False
    deactivate_order: bool = False
    sec_type: str = ""
    available_chart_periods: str = ""
    order_description: str = ""
    order_description_with_contract: str = ""
    alert_active: int = 1
    child_order_type: str = ""
    order_clearing_account: str = ""
    size_and_fills: str = ""
    exit_strategy_display_price: str = ""
    exit_strategy_chart_description: str = ""
    average_price: str = ""
    exit_strategy_tool_availability: str = ""
    allowed_duplicate_opposite: bool = False
    order_time: str = ""

    class Config:
        extra = "allow"
        populate_by_name = True


class LiveOrder(BaseModel):
    order_id: int = Field(0, alias="orderId")
    conid: int = 0
    symbol: str = ""
    side: str = ""
    order_type: str = Field("", alias="orderType")
    size: str | float = ""
    total_size: str | float = Field("", alias="totalSize")
    currency: str = ""
    account: str = ""
    tif: str = ""
    order_status: str = Field("", alias="orderStatus")
    order_ccp_status: str = Field("", alias="orderCcpStatus")
    order_status_description: str = Field("", alias="orderStatusDescription")
    price: float = 0.0
    avg_price: float = Field(0.0, alias="avgPrice")

    class Config:
        extra = "allow"
        populate_by_name = True


class LiveOrdersResponse(BaseModel):
    orders: list[LiveOrder] = Field(default_factory=list)
    snapshot: bool = True

    class Config:
        extra = "allow"
        populate_by_name = True


class CancelOrderResponse(BaseModel):
    msg: str
    order_id: int = 0
    conid: int = 0
    account: str | None = None

    class Config:
        extra = "allow"
        populate_by_name = True
