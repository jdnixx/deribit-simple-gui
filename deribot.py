"""
Deribit Bot - DERIBOT

A class to hold various features of the bot (using the functions in deribit_api.py),
and execute them in a loop.
"""
from time import sleep
import sys
import trio
import asyncio
from deribit_api import RestClient

# interval (in seconds) for run_loop()
LOOP_INTERVAL = 0.5
# Position limits (bot won't buy/sell over this amount of contracts)
MIN_POSITION = -10000
MAX_POSITION = 10000

# instrument to be traded
# INSTRUMENT = "BTC-PERPETUAL"

TICK_SIZE = 0.25

CLIENT = RestClient("AHoDez9QDVyM", "UQT5ZLCGE4WTF6XYSKTJZSJKOCXQES35", "https://test.deribit.com")  # key, secret, URL
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
        # self.display_positions()

    def run(self):
        try:
            trio.run(self.run_loop)
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

    def display_positions(self):
        position = self.client.positions()[0]

        self.pos_size = position['size']
        self.pos_amt = position['amount']
        self.average_price = position['averagePrice']
        self.liq_price = position['estLiqPrice']

        print("%d USD " % self.pos_amt + ("Long" if position['direction'] == 'buy' else "Short") + " from entry %.2f" % self.average_price)

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
            sys.stdout.write("-----\n")
            sys.stdout.flush()

            await trio.sleep(LOOP_INTERVAL)

            # retrieve position on each loop
            self.display_positions()
            print("lolol ", ctr)
            ctr = ctr+1