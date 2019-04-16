import tkinter as tk

import asyncio
import trio

from deribot import OrderManager


"""
INITIAL DECLARATIONS
"""
INSTRUMENT = 'BTC-PERPETUAL'
LOOP_INTERVAL = 0.5

# tk.Panel dimensions
HEIGHT = 700
WIDTH = 800

# The Main Loop
loop = asyncio.get_event_loop()
# OrderManager instance
om = OrderManager(INSTRUMENT)


"""
BUTTON TYPES
inherit from parent tk.Button
"""
class MarketBuyButton(tk.Button):
    def __init__(self, master, amt, **kwargs):
        tk.Button.__init__(self, master, command=om.market_buy(amt),
                        **kwargs)
        self.config(text="Market Buy %d" % amt,
                    bg="lightgreen",
                    activebackground="green")


class MarketSellButton(tk.Button):
    def __init__(self, master, amt, **kwargs):
        tk.Button.__init__(self, master, command=om.market_sell(amt), text="Market Sell %d" % amt,
                        bg="firebrick",
                        activebackground="maroon", **kwargs)


class LimitChaseBuyButton(tk.Button):
    def __init__(self, master, amt, **kwargs):
        tk.Button.__init__(self, master, command=om.limit_chase_buy(amt), text="Limit CHASE Buy %d" % amt,
                        bg="lightgreen",
                        activebackground="green", **kwargs)


class LimitBuyButton(tk.Button):
    def __init__(self, master, amt, **kwargs):
        self.price = om.get_highest_bid()
        tk.Button.__init__(self, master, command=om.limit_buy(amt, self.price),
                        **kwargs)
        self.config(text="Limit Buy %d at $%.2f" % (amt, self.price),
                    bg="lightgreen",
                    activebackground="green")


"""
EVENT CALLS
"""
def left_click(event):
    print("left")


"""
TKINTER STUFF
"""
root = tk.Tk()
root.geometry("%dx%d+%d+%d" % (WIDTH, HEIGHT, 0, -1000))

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
frame = tk.Frame(root, bg='lightblue')
textbox = tk.Text(frame)

# bind leftclick to
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

# grid placements

button_b1k.grid(row=0, ipadx=5, ipady=5, padx=5, pady=5)
button_b2k.grid(row=1, ipadx=5, ipady=5, padx=5, pady=5)
button_b1k_l.grid(row=1, ipadx=5, ipady=5, padx=5, pady=5)
# button_b1k_lc.grid(row=1, ipadx=5, ipady=5, padx=5, pady=5)

button_s1k.grid(row=0, column=1, ipadx=5, ipady=5, padx=5, pady=5)



"""
L O O P functions
"""
async def runloop(func):
    """
    wraps a regular old function into a fully async-compatible func
    """
    func = asyncio.coroutine(func)  # it's a coroutine now

    # return async-wrapped function "func"
    def wrapper(*args, **kwargs):
        return loop.run_until_complete(func(*args, **kwargs))
    return wrapper


async def run_tk(root, interval=0.05):
    """
    Substitutes for root.mainloop() in tkinter
    Makes it async, basically
    """
    while True:
        root.update()
        await asyncio.sleep(interval)

async def main():
    await run_tk(root)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())

# trio.run(om.run_loop)













