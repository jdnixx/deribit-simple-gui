
import asyncio

from ordermanager_interface import OrderManager, NewClient
from pyqt_testing import pyqtwindow

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

omBTC = OrderManager(INSTRUMENT_BTC, client)
# guirootBTC = #? TODO
# omETH = ordermanager_interface.OrderManager(INSTRUMENT, client)
# guirootETH = WindowMarketbuy(omETH)





















async def main():
    # try/except keeps program exit from printing an ugly stacktrace.
    # Also adds a newline to the log on exit
    try:
        if omBTC and guirootBTC:
            await guirootBTC.run()
        if omETH and guirootETH:
            await guirootETH.run()
    except (KeyboardInterrupt, SystemExit, Exception) as e:
        logger.error(e)
        logger.warning("Program exit with above error.")
        logger.warning("\n")
    finally:
        logger.warning("Program exit.")
        logger.warning("\n")

    # while True:
    #     await pm_run
    #     await tk_run


if __name__ == '__main__':
    logger.info("asyncio.run(main()) STARTED!")
    asyncio.run(main())