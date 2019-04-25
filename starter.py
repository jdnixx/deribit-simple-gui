"""
STARTER - Main Container

Main module that bootstraps the program.

*currently used for testing, mostly*
I'm experimenting with GUI changes, so this separates the bot startup from the Tkinter window
"""
import time
import asyncio

from window_marketbuy import WindowMarketbuy, tk
from deribot import OrderManager

import random

"""
INITIAL DECLARATIONS
"""
INSTRUMENT = 'BTC-PERPETUAL'
LOOP_INTERVAL = 0.5

# The Main Loop
loop = asyncio.get_event_loop()
# OrderManager instance
om = OrderManager(INSTRUMENT)
# WindowMarketbuy instance
gui = WindowMarketbuy(om)  # send OrderManager to Window


# "Add Button" button; purely for testing
def dynamically_add_buttons():
    gui.new_marketbutton(random.choice([100,200,300,400,500]),
                         random.choice(["buy", "sell"]))
    gui.place_buttons()


addbutton = tk.Button(gui.frame, text="Add A Button :)", command=lambda: dynamically_add_buttons())
gui.buttons.append(addbutton)



# buttons creation

mktbuy_1 = gui.new_marketbutton(1000, "buy")

# grid placements

gui.place_buttons()

# mktbuy_1.grid(row=0, ipadx=5, ipady=5, padx=5, pady=5)

# mktbuy_2.grid(row=1, ipadx=5, ipady=5, padx=5, pady=5)
# limitbuy.grid(row=1, ipadx=5, ipady=5, padx=5, pady=5)
#
# button_s1k.grid(row=0, column=1, ipadx=5, ipady=5, padx=5, pady=5)

async def main():
    omrun = asyncio.create_task(om.run())
    runtk = asyncio.create_task(gui.run_tk())
    await asyncio.gather(omrun, runtk)


if __name__ == '__main__':
    asyncio.run(main())
