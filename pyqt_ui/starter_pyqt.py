"""
STARTER_PYQT - Main Container Interface

Mainly for starting the pyqt GUI w/ asyncio

"""
import asyncio

from ordermanager_interface import OrderManager, NewClient
from pyqt_ui import uihandler
from utils import log

logger = log.setup_custom_logger(__name__)
logger.info("\n\n Begin")
logger.info("STARTING PROGRAM")

### CONSTANTS ###
INSTRUMENTS = {
    'btc': 'BTC-PERPETUAL',
    'eth': 'ETH-PERPETUAL'
}


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

        # try/except keeps program exit from printing an ugly stacktrace.
        # Also adds a newline to the log on exit
        try:
            logger.info("asyncio.run() STARTING!")
            asyncio.run(self.go())
        except (KeyboardInterrupt, SystemExit, Exception) as e:
            logger.error("Error encountered:")
            logger.error(e)
        finally:
            logger.warning("Program exit.")
            logger.warning("\n")

    async def go(self):
        logger.info("Starter.go() INITIATED!")
        asyncio.create_task(printblah())
        await self.gui.run_asyncqt()

async def printblah():
    while True:
        print("printblah")
        await asyncio.sleep(2)