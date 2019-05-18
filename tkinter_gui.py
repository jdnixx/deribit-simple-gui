import tkinter as tk
import time
import asyncio
# import concurrent.futures
from threading import Timer

from ordermanager_interface import OrderManager
from extras.orders_async import *

DEFAULT_INSTRUMENT = 'BTC-PERPETUAL'
LOOP_INTERVAL = 0.020   # ms
#               ^^^^^ 0.020 works well (20ms)

# tk.Panel dimensions
HEIGHT = 700
WIDTH = 800

# geom = "%dx%d+%d+%d" % (WIDTH, HEIGHT, 0, -1000)
geom = "%dx%d" % (WIDTH, HEIGHT)

"""
EVENT CALLS
"""
def left_click(event):
    print("left")

# bind leftclick to
# frame.bind("<Button-1>", left_click)

# ACTS AS THE ROOT: i.e. root = tk.Tk()
class WindowMarketbuy(tk.Tk):
    om = OrderManager(DEFAULT_INSTRUMENT)

    def __init__(self, ordermanager=None):
        if ordermanager:
            __class__.om = ordermanager
        self.om = __class__.om
        # tk.Tk (root) init
        super().__init__()
        self.geometry(geom)

        # Order.instrument = self.om.instrument
        # Order.client = self.om.client

        BuySellButton.om = self.om
        Order.om = self.om


        ### TKINTER ELEMENTS CREATION ###
        self.frame = tk.Frame(self, bg='lightblue')
        self.frame.place(relwidth=0.5, relheight=0.8, relx=0.1, rely=0.1)

        # self.textbox = tk.Text(self.frame)
        # self.textbox.place(relx=0, rely=0.5, relwidth=0.9, relheight=0.4)

        # create buttons dict
        self.buttons = []

    ### BUTTON METHODS ###
    def place_buttons(self):
        for b in self.buttons:
            b.grid(ipadx=5, ipady=5, padx=5, pady=5)

    def add_button(self, *buttons):
        """add one or multiple Button objects."""
        for b in buttons:
            self.buttons.append(b)

    def new_market_button(self, side, amt):
        b = MarketButton(self.frame, side, amt)
        return b

    def new_limitchase_button(self, side, amt):
        b = LimitChaseButton(self.frame, side, amt)
        return b


    ### RUNTIME METHODS ###
    async def run(self):
        # log_timer = Timer(3, lambda: print("GUI loop running: @ time {0}".format(time.perf_counter())))
        # log_timer.start()
        t = time.time()
        while True:
            await self.run_tk()
            if time.time()-t > 3:
                print("GUI loop running: @ time {0}".format(time.perf_counter()))
                t = time.time()
            # await self.om.run()

    async def run_tk(self):
        """
        Substitutes for root.mainloop() in tkinter. (Makes it async, basically)
        """
        # limitbuy.update_price()

        self.update()
        # print("GUI loop has run: @ time {0}".format(time.perf_counter()))
        await asyncio.sleep(0)


class BuySellButton(tk.Button):
    om = None
    def __init__(self, master, side, amt):
        super().__init__(master)
        self.side = side
        self.amt = amt
        if side == 'buy':
            self.config(text="<orderType> Buy %d" % self.amt,
                        bg="lightgreen",
                        activebackground="green")
        elif side == 'sell':
            self.config(text="<orderType> Sell %d" % self.amt,
                        bg="firebrick",
                        activebackground="maroon")
        else:
            raise ValueError("'side' parameter must be either 'buy' or 'sell'")

class MarketButton(BuySellButton):
    def __init__(self, master, side, amt):
        super().__init__(master, side, amt)
        self.config(text=f"Market {self.side} {self.amt}",
                    command=lambda : self._make())

    def _make(self):
        ordertask = asyncio.create_task(self.om.market_order(self.side, self.amt))
        print(ordertask)

class LimitChaseButton(BuySellButton):
    def __init__(self, master, side, amt):
        super().__init__(master, side, amt)
        self.config(text=f"Limit CHASE {self.side} {self.amt}",
                    command=lambda : self._make())

    def _make(self):
        ordertask = asyncio.create_task(self.om.limit_chase(self.side, self.amt))
        print(ordertask)