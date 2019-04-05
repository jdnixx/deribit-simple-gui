from tkinter import *

# set up RestClient
from deribit_api import RestClient

client = RestClient("AHoDez9QDVyM", "UQT5ZLCGE4WTF6XYSKTJZSJKOCXQES35", "https://test.deribit.com")  # key, secret, URL
client.index()
client.account()
# print(client.positions())

HEIGHT = 700
WIDTH = 800


class OrderManager:
	def __init__(self, element=None):
		self.element = element
		print("Executed during OrderManager definition")

	def display_positions(self, text):
		text.insert(INSERT, client.positions())


class MarketBuyButton(Button):
	def __init__(self, *args, **kwargs):
		# inherit everything from Button parent
		# also, define buy for BTC-PERPETUAL market buy
		buy = lambda :self.market_buy("BTC-PERPETUAL", "market", 10)
		Button.__init__(self, *args, **kwargs, command=buy)

	def market_buy(self, instrument, orderType, quantity):
		return client.buy(instrument, orderType, quantity)


class MarketSellButton(Button):
	def __init__(self, *args, **kwargs):
		# inherit everything from Button parent
		# also, define sell for BTC-PERPETUAL market sell
		sell = lambda :self.market_sell("BTC-PERPETUAL", "market", 10)
		Button.__init__(self, *args, **kwargs, command=sell)

	def market_sell(self, instrument, orderType, quantity):
		return client.sell(instrument, orderType, quantity)

om = OrderManager()
root = Tk()

canvas = Canvas(root, height=HEIGHT, width=WIDTH)
frame = Frame(root, bg="lightblue")

textbox = Text(frame)

#
# def display_positions():
# 	text1.insert(INSERT, client.positions())


buttonMarketBuy = MarketBuyButton(frame, text="Market Buy")
buttonMarketSell = MarketSellButton(frame, text="Market Sell")

# label = Label(frame, text=client.positions())
# label.place(relx=0, rely=0.5, relwidth=0.9, relheight=0.1)

# packs
canvas.pack()
frame.place(relwidth=0.5, relheight=0.8, relx=0.1, rely=0.1)
textbox.place(relx=0, rely=0.5, relwidth=0.9, relheight=0.4)

buttonMarketBuy.place(relx=0, rely=0, relwidth=0.25, relheight=0.25)
buttonMarketSell.place(relx=0.3, rely=0, relwidth=0.25, relheight=0.25)

root.mainloop()
