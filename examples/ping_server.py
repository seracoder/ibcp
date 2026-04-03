import asyncio

import ibcp
from datetime import datetime

""" This script pings the server every 5 minutes and tries to reauthenticate in case it looses it."""


async def main():

    sleep_interval = 60 * 5
    api = ibcp.REST()
    await api.set_default_account()

    try:
        while True:
            status = await api.ping_server()
            if not status["iserver"]["authStatus"]["authenticated"]:
                await api.re_authenticate()
                await asyncio.sleep(5)
                status = await api.get_auth_status()
                now = datetime.now()
                print(now.strftime("%Y/%m/%d %H:%M:%S") + "  " + str(status))
            await asyncio.sleep(sleep_interval)
    finally:
        await api.close()


if __name__ == "__main__":
    asyncio.run(main())
