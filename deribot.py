"""
DERIBOT - Deribit Bot

A class to hold various features of the bot (using the functions in deribit_api.py),
and execute them in a loop.
"""
import time
import asyncio
from deribit_api import RestClient

# interval (in seconds) for run_loop()
LOOP_INTERVAL = 0.5
# Position limits (bot won't buy/sell over this amount of contracts)
MIN_POSITION = -10000
MAX_POSITION = 10000

TICK_SIZE = 0.25

"""
Deribit Client (deribit_api) setup

Keyfile must have at least 2 lines:
    key on the first line
    secret on the second line
    (optional) "test" on the third line, if using the testnet
"""
PATH_TO_KEYFILE = "../deribit_keys.txt" # assumes keyfile is in parent dir

with open(PATH_TO_KEYFILE, "r") as f:
    deribit_key = f.readline().strip()
    deribit_secret = f.readline().strip()

    optional_test = f.readline().strip()
    if optional_test == "test":
        deribit_testnet = "https://test.deribit.com"
    else:
        deribit_testnet = None

CLIENT = RestClient(deribit_key, deribit_secret, deribit_testnet)   # key, secret, URL


class OrderManager:
    """
    Interface containing all the main "bot"-type (user-facing) methods
    """
    def __init__(self, instrument):
        self.instrument = instrument

        self.client = CLIENT
        self.client.index()
        self.client.account()

        # initialize position var
        self.position = self.get_position_details()     # this will also run on each async loop in starter.py()
        self.ctr = 0

        print("^OrderManager.__init__() completed run!\n")

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
    def _get_position(self):
        """
        internal method for retrieving current position data from client
        :return: dict of your first current position
        """
        return self.client.positions()[0]

    def _get_orderbook(self):
        return self.client.getorderbook(self.instrument)

    def get_position_details(self):
        pos = self._get_position()
        amt_USD = int(pos['amount'])
        direction = pos['direction']
        entry = pos['averagePrice']
        liq_price = pos['estLiqPrice']

        print("{:d} USD {:s} from entry ${:.2f}. (Liquidation at ~${:.2f})".format(amt_USD, direction, entry, liq_price))
        return pos
        # # prints every 10 seconds
        # await asyncio.sleep(10)

    ### ORDER BOOK METHODS ###
    def get_highest_bid(self):
        book = self._get_orderbook()
        return book['bids'][0]['price']

    ### MAKE-ORDER METHODS ###
    def market_buy(self, amt):
        return lambda: self.client.buy(self.instrument, "market", self.qty(amt))

    def market_sell(self, amt):
        return lambda: self.client.sell(self.instrument, "market", self.qty(amt))

    def stop_market_buy(self, amt, stopPx, reduce_only=None):
        return self.client.buy(self.instrument, "stop_market", self.qty(amt), stopPx, reduce_only)

    def stop_market_sell(self, amt, stopPx, reduce_only=None):
        return self.client.sell(self.instrument, "stop_market", self.qty(amt), stopPx, reduce_only)

    def limit_buy(self, amt, price, postOnly=None):
        return lambda: self.client.buy(self.instrument, "limit", self.qty(amt), price, postOnly)

    def limit_sell(self, amt, price, postOnly=None):
        return lambda: self.client.sell(self.instrument, "limit", self.qty(amt), price, postOnly)


    ### STOPS (LOOP) METHODS ###
    def doomsday_stop_monitor(self):
        pass

    async def limit_chaser_loop(self):
        print(self.get_highest_bid())
        print("ok bid gotten")

    async def limit_chase_buy(self, amt):
        startprice = self.get_highest_bid()
        price = startprice
        order = self.limit_buy(amt, startprice, postOnly=True)['order']
        orderid = order['orderId']
        price = order['price']
        print(order)

        await self.limit_chaser_loop



    ### MAIN ORDERMANAGER METHODS ###
    async def run(self):
        while True:
            await self.run_loop()

    async def run_loop(self):
        # update & display position
        # await self.print_position_details()
        self.get_position_details()

        print("deribot loop has run: @ time {0} (ctr = {1})".format(time.perf_counter(), self.ctr))
        self.ctr += 1
        # loop every LOOP_INTERVAL seconds
        await asyncio.sleep(0.5)