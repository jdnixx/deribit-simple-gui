"""
Order Manager Interface - deribit API client wrapper, with my own custom-built features/functions
"""

import time
import asyncio
from extras.deribit_api import RestClient
from extras.position_monitor import Monitor

# interval (in seconds) for run_loop()
LOOP_INTERVAL = 0.5
# Position limits (bot won't buy/sell over this amount of contracts)
MIN_POSITION = -10000
MAX_POSITION = 10000

TICK_SIZES = {
    'BTC-PERPETUAL': 0.25,
    'ETH-PERPETUAL': 0.01
}


class OrderManager:
    """
    Interface containing all the main "bot"-type (user-facing) methods

    :param instrument: the swap to be traded on ('BTC-PERPETUAL', 'ETH-PERPETUAL')
    """
    def __init__(self, instrument):
        self.instrument = instrument
        self.ticksize = TICK_SIZES[instrument]

        self.client = create_client()
        self.client.index()
        self.client.account()

        # self.pm = Monitor()           nope, this is for spawning individually




        # initialize position var
        # self.position = self.get_position_details()     # this will also run on each async loop in starter.py()
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
    def get_orderbook(self):
        return self.client.getorderbook(self.instrument)

    def get_highest_bid_price(self):
        book = self.get_orderbook()
        return book['bids'][0]['price']

    def get_highest_ask_price(self):
        book = self.get_orderbook()
        return book['asks'][0]['price']

    ### PLACE-ORDER METHODS ###
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


    ### SPECIAL ORDERS ###
    async def limit_chase_buy(self, amt):
        startprice = self.get_highest_bid()
        price = startprice
        order = self.limit_buy(amt, startprice, postOnly=True)['order']
        orderid = order['orderId']
        price = order['price']
        print(order)

        await self.limit_chaser_loop


    ### STOPS (LOOP) METHODS ###
    async def create_monitor(self):
        pass





    ### MAIN ORDERMANAGER METHODS ###
    async def run(self):

        while True:
            await self.run_loop()

    async def run_loop(self):
        # update & display position
        # await self.print_position_details()
        # self.get_position_details()

        print("deribot loop has run: @ time {0} (ctr = {1})".format(time.perf_counter(), self.ctr))
        self.ctr += 1
        # loop every LOOP_INTERVAL seconds
        await asyncio.sleep(0.5)



def create_client():
    """
    Deribit Client setup

    Keyfile must have at least 2 lines:
        key on the first line
        secret on the second line
        (optional) "test" on the third line, if using the testnet

    :return: an instance of the Deribit RestClient
    """
    path_to_keyfile = "../deribit_keys.txt"  # assumes keyfile is in parent dir

    with open(path_to_keyfile, "r") as f:
        deribit_key = f.readline().strip()
        deribit_secret = f.readline().strip()

        optional_test = f.readline().strip()
        if optional_test == "test":
            deribit_testnet = "https://test.deribit.com"
        else:
            deribit_testnet = None

    client = RestClient(deribit_key, deribit_secret, deribit_testnet)  # key, secret, URL
    return client