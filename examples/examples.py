# IBCP Examples
# This file contains examples of how to use the IBCP library

import asyncio

import src.ibcp as ibcp


async def main():
    # Create a REST client
    api = ibcp.REST(url="http://localhost:5001")
    await api.set_default_account()
    # default parameters: url="http://localhost:5000", ssl=False
    # SSL warnings can be suppressed by setting up a SSL certificate

    # Example: Get historical data
    bars = (await api.get_bars("TSLA")).data
    print(bars)

    # Example: Submit orders
    # orders = [
    #     {
    #         "conid": await api.get_conid("TSLA"),
    #         "orderType": "MKT",
    #         "side": "BUY",
    #         "quantity": 6,
    #         "tif": "GTC",
    #     }
    # ]
    # result = await api.submit_orders(orders)
    # print(result)

    # Example: Modify order
    # order = {
    #     "conid": await api.get_conid("TSLA"),
    #     "orderType": "MKT",
    #     "side": "BUY",
    #     "quantity": 7,
    #     "tif": "GTC",
    # }
    # result = await api.modify_order(order_id=1258176647, order=order)
    # print(result)

    # Example: Get order status
    # order_status = await api.get_order(1258176647)
    # print(order_status)

    # Example: Get live orders
    # live_orders = await api.get_live_orders()
    # print(live_orders)

    await api.close()

    print("IBCP examples loaded successfully!")
    print("Uncomment the examples above to run them.")


if __name__ == "__main__":
    asyncio.run(main())
