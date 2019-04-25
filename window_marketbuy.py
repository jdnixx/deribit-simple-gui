import tkinter as tk
import time
import asyncio
import trio

"""
INITIAL DECLARATIONS
"""
INSTRUMENT = 'BTC-PERPETUAL'
LOOP_INTERVAL = 0.5

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


"""
TKINTER STUFF
"""


# ACTS AS THE ROOT
# functionally the same as: root = tk.Tk()
class WindowMarketbuy(tk.Tk):
    def __init__(self, ordermanager):
        tk.Tk.__init__(self)
        self.geometry("%dx%d+%d+%d" % (WIDTH, HEIGHT, 0, -1000))

        # set OrderManager object
        self.om = ordermanager

        # CREATE THE MAIN FRAME !!!
        self.frame = self.NewFrame(self, bg='lightblue')

        """
        BUTTONS
        """
        # create buttons dict
        self.buttons = []

        # packs
        self.frame.place(relwidth=0.5, relheight=0.8, relx=0.1, rely=0.1)
        self.textbox = tk.Text(self.frame)
        self.textbox.place(relx=0, rely=0.5, relwidth=0.9, relheight=0.4)

    class NewFrame(tk.Frame):
        def __init__(self, master, **kwargs):
            tk.Frame.__init__(self, master, **kwargs)

    def new_marketbutton(self, amt, ordertype=None):
        newbutton = tk.Button(self.frame)
        if ordertype == "buy":
            newbutton.config(command=self.om.market_buy(amt),
                             text="Market Buy %d" % amt,
                             bg="lightgreen",
                             activebackground="green")
        elif ordertype == "sell":
            newbutton.config(command=self.om.market_sell(amt),
                             text="Market Sell %d" % amt,
                             bg="firebrick",
                             activebackground="maroon")
        else:
            raise TypeError('Button ordertype required ("buy" or "sell")')
        self.buttons.append(newbutton)

    class GenericButtonFactory(tk.Button):
        def __init__(self):
            tk.Button.__init__(self.master)

    def place_buttons(self):
        for b in self.buttons:
            b.grid(ipadx=5, ipady=5, padx=5, pady=5)


    async def run_tk(self, interval=0.020):
        """
        Substitutes for root.mainloop() in tkinter
        Makes it async, basically
        :param: interval = 0.020 works well
        """
        while True:
            # limitbuy.update_price()

            self.update()
            await asyncio.sleep(interval)

            # print("GUI loop has run: time", time.perf_counter())


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
