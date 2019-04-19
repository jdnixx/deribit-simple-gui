"""
Deribit Bot - DERIBOT

A class to hold various features of the bot (using the functions in deribit_api.py),
and execute them in a loop.
"""
import sys
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
---
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

CLIENT = RestClient(deribit_key, deribit_secret, deribit_testnet) # key, secret, URL
# self.client.index()
# self.client.account()


class OrderManager:
    '''

    '''
    def __init__(self, instrument):
        self.instrument = instrument

        self.client = CLIENT
        self.client.index()
        self.client.account()
        self.refresh_position_details()
        print("^Init run!\n")

    async def run(self):
        try:
            await self.run_loop()
        except KeyboardInterrupt:
            sys.exit()

    def qty(self, amt):
        '''
        Checks if instrument is BTC-PERPETUAL and if so, returns $10 contracts (instead of $1)

        :param amt: the amount of USD to be converted into $10 contracts
        '''
        if self.instrument == 'BTC-PERPETUAL':
            return amt / 10
        else:
            return amt

    def get_position(self):
        return self.client.positions()[0]

    def refresh_position_details(self):
        pos = self.get_position()
        self.pos_size_contracts = pos['size']
        self.pos_amt_USD = pos['amount']
        self.entry = pos['averagePrice']
        self.liq_price = pos['estLiqPrice']

        # purely for console logging purposes - should be replaced with
        print("%d USD " % self.pos_amt_USD + pos['direction'] + " from entry %.2f" % self.entry)

    def short_limit_exceeded(self):
        return

    def long_limit_exceeded(self):
        return

    def get_highest_bid(self):
        book = self.client.getorderbook(self.instrument)
        return book['bids'][0]['price']

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

    def doomsday_stop_monitor(self):
        return

    async def limit_chase_buy(self, amt):
        startprice = self.get_highest_bid()
        price = startprice
        order = self.limit_buy(amt, startprice, postOnly=True)['order']
        orderid = order['orderId']
        price = order['price']
        print(order)

        await self.limit_chaser_loop

    async def limit_chaser_loop(self):
        print(self.get_highest_bid())
        await trio.sleep(5)
        print("ok bid gotten")

    async def run_loop(self):
        ctr = 0
        while True:
            # sys.stdout.write("-----\n")
            # sys.stdout.flush()

            # update & display position on each loop
            # self.refresh_position_details()

            # print("lolol ",ctr)
            ctr = ctr+1

            print("deribot loop has run: time", time.perf_counter())

            # await trio.sleep(LOOP_INTERVAL)
            await asyncio.sleep(1)