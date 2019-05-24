"""
Order Manager Interface - deribit API client wrapper, with my own custom-built features/functions
"""

from extras.deribit_api_async import RestClient
from extras.orders_async import *

from utils import log


# Constants
DEFAULT_INSTRUMENT = 'BTC-PERPETUAL'
# interval (in seconds) for run_loop()
LOOP_INTERVAL = 0.5
# Position limits (bot won't buy/sell over this amount of contracts)
MIN_POSITION = -10000
MAX_POSITION = 10000

TICK_SIZES = {
    'BTC-PERPETUAL': 0.25,
    'ETH-PERPETUAL': 0.01
}


# Logging
logger = log.setup_custom_logger(__name__)


class OrderManager:
    """
    Interface containing all the main "bot"-type (user-facing) methods

    :param instrument: the swap to be traded on ('BTC-PERPETUAL', 'ETH-PERPETUAL')
    """
    def __init__(self, client=None, instrument=None, path_to_keyfile=None):
        self.client = client
        self.instrument = instrument

        if not client:
            if not path_to_keyfile:
                self.client = NewClient()   # by default uses 'deribit_keys.txt'
            else:
                self.client = NewClient(path_to_keyfile)
        if not instrument:
            self.instrument = DEFAULT_INSTRUMENT
        self.client.index()
        self.client.account()


        self.ticksize = TICK_SIZES[self.instrument]  # not used yet


        logger.info("OM object created!")

    def qty(self, amt):
        """
        Checks if instrument is BTC-PERPETUAL and if so, returns a quantity of $10 contracts (instead of $1)
        :param amt: the amount of USD to be converted into $10 contracts
        :return:
        """

        if self.instrument == 'BTC-PERPETUAL':
            return amt / 10
        else:
            return amt

    def short_limit_exceeded(self):
        return

    def long_limit_exceeded(self):
        return


    ### POSITION METHODS ###
    def get_position(self):
        """
        Retrieve the current position data from client.
        :return: dict of your first current position
        """
        return self.client.positions()[0]

    def print_position_details(self):
        """Returns the actual position dict, and prints some key deets"""
        pos = self.get_position()
        amt_USD = int(pos['amount'])
        direction = pos['direction']
        entry = pos['averagePrice']
        liq_price = pos['estLiqPrice']

        print("{:d} USD {:s} from entry ${:.2f}. (Liquidation at ~${:.2f})".format(amt_USD, direction, entry, liq_price))
        return pos
        # # prints every 10 seconds
        # await asyncio.sleep(10)

    ### ORDER BOOK METHODS ###
    async def get_orderbook(self):
        return await self.client.getorderbook(self.instrument)

    async def get_spread_price(self, side):
        book = await self.get_orderbook()
        return book[BOOK_SIDE_ORDERTYPE[side]][0]['price']

    ### PLACE-ORDER METHODS ###
    async def market_order(self, side, amt, reduceOnly=None, label=None):
        return await MarketOrder().make_market_order(side, amt, reduceOnly=reduceOnly, label=label)

    async def limit(self, side, amt, price, postOnly=None, reduceOnly=None, label=None):
        return await LimitOrder().make_limit_order(side, amt, price, postOnly=postOnly, reduceOnly=reduceOnly, label=label)

    async def limit_chase(self, side, amt, reduceOnly=None, label=None):
        limchase_instance = LimitChaser()
        await limchase_instance.make_limitchase_initial_order(side, amt, reduceOnly=reduceOnly, label=label)

        # start loop
        while not await limchase_instance.is_filled():
            logger.info("limit_chase() is running...")
            await limchase_instance.spam_edit_order()
            logger.info("LimitChaser loop sleeping for 50ms...")
            await asyncio.sleep(0.05)
        logger.info("LimitChase done, final order: ")
        logger.info(limchase_instance.order)
        return limchase_instance.order  # order must be filled

    # def stop_market_buy(self, amt, stopPx, reduce_only=None):
    #     return self.client.buy(self.instrument, "stop_market", self.qty(amt), stopPx, reduce_only)
    #
    # def stop_market_sell(self, amt, stopPx, reduce_only=None):
    #     return self.client.sell(self.instrument, "stop_market", self.qty(amt), stopPx, reduce_only)

    ### STOPS (LOOP) METHODS ###
    async def create_monitor(self):
        pass

    ### MAIN ORDERMANAGER METHODS ###
    # async def run(self):
    #     t = time.time()
    #     while True:               # removed this loop, instead placed loop in WindowMarketBuy.run()
    #         await self.run_loop()
    #         if time.time() - t > 3:  # print every 3 seconds
    #             logger.info("OM loop running: @ time {0}".format(time.perf_counter()))
    #             t = time.time()
    #         await self.run_loop()

    async def run_loop(self):
        # update & display position
        # await self.print_position_details()
        # self.get_position_details()

        # print("deribot loop has run: @ time {0} (ctr = {1})".format(time.perf_counter(), self.ctr))
        # self.ctr += 1
        # loop every LOOP_INTERVAL seconds
        await asyncio.sleep(LOOP_INTERVAL)


class NewClient(RestClient):
    """
    Deribit Client setup

    Keyfile must have at least 2 lines:
        key on the first line
        secret on the second line
        (optional) "test" on the third line, if using the testnet

    :return: an instance of the Deribit RestClient
    """
    def __init__(self, path_to_keyfile="../deribit_keys.txt"):

        # assumes keyfile is in parent dir

        with open(path_to_keyfile, "r") as f:
            deribit_key = f.readline().strip()
            deribit_secret = f.readline().strip()
            optional_test = f.readline().strip()

            if optional_test == "test":
                deribit_testnet = "https://test.deribit.com"
            else:
                deribit_testnet = None

        super().__init__(deribit_key, deribit_secret, deribit_testnet)  # key, secret, URL
        logger.info('New Client created!')