from tkinter import *
from tkinter import ttk

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
om.run_loop()


class MarketBuyButton(Button):
    """
    inherit everything from Button parent, but add:

    :param qty:
        Quantity of contracts (USD) to be placed when button is clicked.
    """

    def __init__(self, master, amt, **kwargs):
        self.amt = amt
        self.qty = amt / 10
        Button.__init__(self, master, command=om.market_buy(amt), text="Market Buy %d" % self.amt,
                        bg="lightgreen",
                        activebackground="green", **kwargs)

    # def market_buy(self):
    #     return lambda: client.buy("BTC-PERPETUAL", "market", self.qty)


class MarketSellButton(Button):
    """
    inherit everything from Button parent, but add:

    :param qty:
        Quantity of contracts (USD) to be placed when button is clicked.
    """

    def __init__(self, master, amt, **kwargs):
        self.amt = amt
        self.qty = amt / 10
        Button.__init__(self, master, command=om.market_sell(amt), text="Market Sell %d" % self.amt,
                        bg="firebrick",
                        activebackground="maroon", **kwargs)

    # def market_sell(self):
    #     return lambda: client.sell("BTC-PERPETUAL", "market", self.qty)


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

button_s1k = MarketSellButton(frame, 1000)


button_b1k.grid(row=0, ipadx=5, ipady=5, padx=5, pady=5)
button_b2k.grid(row=1, ipadx=5, ipady=5, padx=5, pady=5)

button_s1k.grid(row=0, column=1, ipadx=5, ipady=5, padx=5, pady=5)

# button_b1k.place(relx=0, rely=0, relwidth=0.25, relheight=0.25)
# button_b2k.place(relx=0, rely=0, relwidth=0.25, relheight=0.25)

# button_s1k.place(relx=0.3, rely=0, relwidth=0.25, relheight=0.25)





#
root.mainloop()


