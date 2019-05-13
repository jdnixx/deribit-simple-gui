import tkinter as tk
import time
import asyncio
import concurrent.futures

from ordermanager_interface import OrderManager
from extras.orders import *

LOOP_INTERVAL = 0.020   # ms

# tk.Panel dimensions
HEIGHT = 700
WIDTH = 800

"""
EVENT CALLS
"""
def left_click(event):
    print("left")

# bind leftclick to
# frame.bind("<Button-1>", left_click)

# ACTS AS THE ROOT: i.e. root = tk.Tk()
class WindowMarketbuy(tk.Tk):
    om = OrderManager('BTC-PERPETUAL')
    def __init__(self):
        # assign original OrderManager instance (created in starter.py)
        self.om = __class__.om
        # tk.Tk (root) init
        super().__init__()
        self.geometry("%dx%d+%d+%d" % (WIDTH, HEIGHT, 0, -1000))

        Order.instrument = self.om.instrument
        Order.client = self.om.client


        ### TKINTER ELEMENTS CREATION ###
        self.frame = tk.Frame(self, bg='lightblue')
        self.frame.place(relwidth=0.5, relheight=0.8, relx=0.1, rely=0.1)

        self.textbox = tk.Text(self.frame)
        self.textbox.place(relx=0, rely=0.5, relwidth=0.9, relheight=0.4)
        # create buttons dict
        self.buttons = []

    def place_buttons(self):
        for b in self.buttons:
            b.grid(ipadx=5, ipady=5, padx=5, pady=5)

    def add_button(self, *buttons):
        """add one or multiple Button objects."""
        for b in buttons:
            self.buttons.append(b)

    def new_market_button(self, side, amt):
        b = MarketButton(self.frame, side, amt)
        # b.amt = amt # have to run config again???
        return b

    # def new_sell_market_button(self, amt):
    #     b = MarketSellButton(self.frame)
    #     b.amt = amt
    #     return b
    #
    def new_limitchase_button(self, side, amt):
        b = LimitChaseButton(self.frame, side, amt, fn=lambda: asyncio.create_task(self.om.limit_chase(side, amt)))
        # b.amt = amt # have to run config again???
        return b

    # class NewFrame(tk.Frame):
    #     def __init__(self, master, **kwargs):
    #         tk.Frame.__init__(self, master, **kwargs)

    async def run(self):
        while True:
            await self.run_tk()
            await self.om.run()

    async def run_tk(self, interval=0.2):
        """
        Substitutes for root.mainloop() in tkinter. (Makes it async, basically)
        :param: interval = to sleep, 0.020 works well (20ms)
        """
        # limitbuy.update_price()

        self.update()
        print("GUI loop has run: @ time {0}".format(time.perf_counter()))
        await asyncio.sleep(interval)


class BuySellButton(tk.Button):
    def __init__(self, master, side):
        super().__init__(master)
        self.amt = 0
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
        super().__init__(master, side)
        self.amt = amt
        self.config(text=f"Market {side} {self.amt}",
                    command=lambda: MarketOrder(side, self.amt))

class MarketSellButton(BuySellButton):
    def __init__(self, master, side):
        super().__init__(master, side)
        self.config(text="Market Sell %d" % self.amt,
                    bg="firebrick",
                    activebackground="maroon")

class LimitChaseButton(BuySellButton):
    def __init__(self, master, side, amt, fn):
        super().__init__(master, side)
        self.amt = amt
        self.config(text=f"Limit CHASE {side} {self.amt}",
                    command=fn)
                    # command=lambda: asyncio.create_task(WindowMarketbuy.om.limit_chase(side, self.amt)))
"""
BUTTON TYPES
inherit from parent tk.Button
"""

# class LimitChaseBuyButton(BuySellButton):
#     def __init__(self, master, amt, **kwargs):
#         BuySellButton.__init__(self, master, command=self.om.limit_chase_buy(amt),
#                                       text="Limit CHASE Buy %d" % amt,
#                                       bg="lightgreen",
#                                       activebackground="green", **kwargs)
#
#
# class LimitBuyButton(BuySellButton):
#     def __init__(self, master, amt, **kwargs):
#         self.price = self.om.get_highest_bid()
#         self.amt = amt
#         BuySellButton.__init__(self, master, command=self.om.limit_buy(self.amt, self.price),
#                                       **kwargs)
#         self.update_price()
#
#     def update_price(self):
#         self.price = self.om.get_highest_bid()
#         self.config(text="Limit Buy %d at $%.2f" % (self.amt, self.price),
#                     bg="lightgreen",
#                     activebackground="green")


"""
L O O P functions
"""

"""
UNUSED
"""
# frame.after(0, after_method_example)


# root.mainloop()


# def after_method_example():
#     print("After method!!")
#     print(asyncio.get_event_loop())
#     frame.after(2000, after_method_example)
#
#
# async def convert_func_to_async(func):
#     """
#     wraps a regular old function into a fully async-compatible func
#
#     ** NOT CURRENTLY USED **
#
#     """
#     func = asyncio.coroutine(func)  # it's a coroutine now
#
#     # return async-wrapped function "func"
#     def wrapper(*args, **kwargs):
#         # return loop.run_until_complete(func(*args, **kwargs))
#
#     return wrapper
