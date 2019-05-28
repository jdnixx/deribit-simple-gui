"""
STARTER_PYQT - Main Container Interface

WARNING!!!!!!!!!!!
Works on live accounts!
Only use a keyfile with testnet credentials if you aren't ready for live trading yet.

(This program may be unfinished or buggy; use at your own risk)

"""
import asyncio

from ordermanager_interface import OrderManager, NewClient
from pyqt_ui import uihandler
from utils import log

### LOGGING ###
logger = log.setup_custom_logger(__name__)
logger.info("\n\n Begin")
logger.info("STARTING PROGRAM")

### CONSTANTS ###
INSTRUMENTS = {
    'btc': 'BTC-PERPETUAL',
    'eth': 'ETH-PERPETUAL'
}
# INSTRUMENT_BTC = 'BTC-PERPETUAL'
# INSTRUMENT_ETH = 'ETH-PERPETUAL'
# LOOP_INTERVAL = 0.5


class Starter:
    """ Bootstrapper class that sets up the entire program instance (GUI, OrderManager, etc.)
    for a specified Deribit account and market (BTC or ETH perpetuals).
    :param path_to_keyfile: string, relative path to keyfile containing Deribit API credentials
    :param market: string, either 'btc' or 'eth'
    """
    def __init__(self, path_to_keyfile, market):
        client = NewClient(path_to_keyfile)

        order_manager_instance = OrderManager(client, INSTRUMENTS[market])
        self.gui = uihandler.AsyncQt(order_manager_instance)

        logger.info("asyncio.run() STARTING!")
        asyncio.run(self.go())

    async def go(self):
        logger.info("Starter.go() INITIATED!")
        asyncio.create_task(printblah())
        await self.gui.run_asyncqt()

async def main():
    # try/except keeps program exit from printing an ugly stacktrace.
    # Also adds a newline to the log on exit
    try:
        print('main started somehow')
        asyncio.create_task(printblah())
        # await gui.run_asyncqt()
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

async def printblah():
    while True:
        print("printblah")
        await asyncio.sleep(2)


if __name__ == '__main__':
    logger.info("asyncio.run(main()) STARTED!")
    asyncio.run(main())
    # asyncio.get_event_loop().run_forever()