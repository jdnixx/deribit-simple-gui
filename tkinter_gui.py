import tkinter as tk
import time
import asyncio
import concurrent.futures

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
    om = None
    def __init__(self):
        # assign original OrderManager instance (created in starter.py)
        self.om = __class__.om
        # tk.Tk (root) init
        super().__init__()
        self.geometry("%dx%d+%d+%d" % (WIDTH, HEIGHT, 0, -1000))



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

    def new_buy_market_button(self, amt):
        b = MarketBuyButton(self.frame)
        b.amt = amt # have to run config again???
        return b

    def new_sell_market_button(self, amt):
        b = MarketSellButton(self.frame)
        b.amt = amt
        return b

    def new_buy_limitchase_button(self, amt, max_ticks):
        b = LimitchaseBuyButton(self.frame)

    # class NewFrame(tk.Frame):
    #     def __init__(self, master, **kwargs):
    #         tk.Frame.__init__(self, master, **kwargs)

    async def run(self):
        while True:
            await self.run_tk()

    async def run_tk(self, interval=0.2):
        """
        Substitutes for root.mainloop() in tkinter. (Makes it async, basically)
        :param: interval = to sleep, 0.020 works well (20ms)
        """
        # limitbuy.update_price()

        self.update()
        print("GUI loop has run: @ time {0}".format(time.perf_counter()))
        await asyncio.sleep(interval)


class GenericButtonFactory(tk.Button):
    def __init__(self, master):
        super().__init__(master)
        self.amt = 0

class MarketBuyButton(GenericButtonFactory):
    def __init__(self, master):
        super().__init__(master)
        self.config(text="Market Buy %d" % self.amt,
                    bg="lightgreen",
                    activebackground="green")

class MarketSellButton(GenericButtonFactory):
    def __init__(self, master):
        super().__init__(master)
        self.config(text="Market Sell %d" % self.amt,
                    bg="firebrick",
                    activebackground="maroon")

class LimitchaseBuyButton(GenericButtonFactory):
    def __init__(self, master):
        super().__init__(master)
        self.config(text="Limit CHASE Buy %d" % self.amt,
                    bg="lightgreen",
                    activebackground="green")
"""
BUTTON TYPES
inherit from parent tk.Button
"""

# class LimitChaseBuyButton(GenericButtonFactory):
#     def __init__(self, master, amt, **kwargs):
#         GenericButtonFactory.__init__(self, master, command=self.om.limit_chase_buy(amt),
#                                       text="Limit CHASE Buy %d" % amt,
#                                       bg="lightgreen",
#                                       activebackground="green", **kwargs)
#
#
# class LimitBuyButton(GenericButtonFactory):
#     def __init__(self, master, amt, **kwargs):
#         self.price = self.om.get_highest_bid()
#         self.amt = amt
#         GenericButtonFactory.__init__(self, master, command=self.om.limit_buy(self.amt, self.price),
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
