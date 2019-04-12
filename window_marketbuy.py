from tkinter import *
from tkinter import ttk
import trio
import triotk

# set up RestClient
from deribot import OrderManager
from deribit_api import RestClient

# client = RestClient("AHoDez9QDVyM", "UQT5ZLCGE4WTF6XYSKTJZSJKOCXQES35", "https://test.deribit.com")  # key, secret, URL
# client.index()
# client.account()
# print(client.positions())

HEIGHT = 700
WIDTH = 800


# OrderManager object
om = OrderManager('BTC-PERPETUAL')


"""
BUTTON TYPES

inherit from parent tk.Button
"""
class MarketBuyButton(Button):
    def __init__(self, master, amt, **kwargs):
        Button.__init__(self, master, command=om.market_buy(amt),
                        **kwargs)
        self.config(text="Market Buy %d" % amt,
                    bg="lightgreen",
                    activebackground="green")


class MarketSellButton(Button):
    def __init__(self, master, amt, **kwargs):
        Button.__init__(self, master, command=om.market_sell(amt), text="Market Sell %d" % amt,
                        bg="firebrick",
                        activebackground="maroon", **kwargs)


class LimitChaseBuyButton(Button):
    def __init__(self, master, amt, **kwargs):
        Button.__init__(self, master, command=om.limit_chase_buy(amt), text="Limit CHASE Buy %d" % amt,
                        bg="lightgreen",
                        activebackground="green", **kwargs)


class LimitBuyButton(Button):
    def __init__(self, master, amt, **kwargs):
        self.price = om.get_highest_bid()
        Button.__init__(self, master, command=om.limit_buy(amt, self.price),
                        **kwargs)
        self.config(text="Limit Buy %d at $%.2f" % (amt, self.price),
                    bg="lightgreen",
                    activebackground="green")


def left_click(event):
    print("left")


# tkinter stuff

root = Tk()

canvas = Canvas(root, height=HEIGHT, width=WIDTH)
frame = ttk.Frame(root, padding="3 3 12 12")
textbox = Text(frame)

frame.bind("<Button-1>", left_click)


# packs

canvas.pack()
frame.place(relwidth=0.5, relheight=0.8, relx=0.1, rely=0.1)
textbox.place(relx=0, rely=0.5, relwidth=0.9, relheight=0.4)

# buttons creation

button_b1k = MarketBuyButton(frame, 1000)
button_b2k = MarketBuyButton(frame, 2000)
button_b1k_l = LimitBuyButton(frame, 1000)
# button_b1k_lc = LimitChaseBuyButton(frame, 1000)

button_s1k = MarketSellButton(frame, 1000)


button_b1k.grid(row=0, ipadx=5, ipady=5, padx=5, pady=5)
button_b2k.grid(row=1, ipadx=5, ipady=5, padx=5, pady=5)
button_b1k_l.grid(row=1, ipadx=5, ipady=5, padx=5, pady=5)
# button_b1k_lc.grid(row=1, ipadx=5, ipady=5, padx=5, pady=5)

button_s1k.grid(row=0, column=1, ipadx=5, ipady=5, padx=5, pady=5)

#

# MAIN L0000000000000P
trio.run(om.run_loop)
master_loop = root.mainloop
trio.run(master_loop)
