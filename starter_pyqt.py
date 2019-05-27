
import asyncio

from ordermanager_interface import OrderManager, NewClient
# from pyqt_testing import pyqtwindow
from pyqt_ui import uihandler

from utils import log


# Constants
INSTRUMENT_BTC = 'BTC-PERPETUAL'
INSTRUMENT_ETH = 'ETH-PERPETUAL'
# LOOP_INTERVAL = 0.5

### LOGGING ###
logger = log.setup_custom_logger(__name__)
logger.info("\n\n Begin")
logger.info("STARTING PROGRAM")


### GUI WINDOW SETUP ###
client = NewClient('../deribit_keys.txt')
omBTC = omETH = guirootBTC = guirootETH = None

omBTC = OrderManager(client, INSTRUMENT_BTC)
# guirootBTC = #? TODO
# omETH = ordermanager_interface.OrderManager(INSTRUMENT, client)
# guirootETH = WindowMarketbuy(omETH)


async def main():
    # try/except keeps program exit from printing an ugly stacktrace.
    # Also adds a newline to the log on exit
    try:
        gui = uihandler.AsyncQt()
        asyncio.create_task(printblah())
        asyncio.create_task(gui.run_asyncqt())
        # asyncio.create_task(gui.run_asyncqt())
        # while True:
        #     print(asyncio.get_event_loop())
            # tsk = asyncio.create_task(asyncio.sleep(5))
            # task = asyncio.create_task(printblah())
            # asyncio.gather(tsk, task)

        # app = uihandler.AsyncQt()
        # await app.run_asyncqt()
    except (KeyboardInterrupt, SystemExit, Exception) as e:
        logger.error(e)
        logger.warning("Program exit with above error.")
        logger.warning("\n")
    finally:
        logger.warning("Program exit.")
        logger.warning("\n")

print("blah")

async def printblah():
    while True:
        print("printblah")
        await asyncio.sleep(2)


# async def main():
#     # try/except keeps program exit from printing an ugly stacktrace.
#     # Also adds a newline to the log on exit
#     try:
#         if omBTC and guirootBTC:
#             await guirootBTC.run()
#         if omETH and guirootETH:
#             await guirootETH.run()
#     except (KeyboardInterrupt, SystemExit, Exception) as e:
#         logger.error(e)
#         logger.warning("Program exit with above error.")
#         logger.warning("\n")
#     finally:
#         logger.warning("Program exit.")
#         logger.warning("\n")


if __name__ == '__main__':
    logger.info("asyncio.run(main()) STARTED!")
    asyncio.run(main())
    # asyncio.get_event_loop().run_forever()