"""
STARTER - Main Container

Main module that bootstraps the program.

*currently used for testing, mostly*
I'm experimenting with GUI changes, so this separates the bot startup from the Tkinter window
"""
import time
import asyncio
from concurrent.futures import ThreadPoolExecutor

from tkinter_gui import WindowMarketbuy, tk
from deribot import OrderManager

import random

"""
INITIAL DECLARATIONS
"""
INSTRUMENT = 'BTC-PERPETUAL'
LOOP_INTERVAL = 0.5

# The Main Loop
# loop = asyncio.get_event_loop()

# OrderManager instance
om = OrderManager(INSTRUMENT)
# assign the OrderManager across all Windows
WindowMarketbuy.om = om
guiroot = WindowMarketbuy()


### TKINTER SETUP ###

# "Add Button" button; purely for testing
def dynamically_add_buttons():
    guiroot.add_button(random.choice([
        guiroot.new_buy_market_button(random.choice([100, 200, 300, 400, 500])),
        guiroot.new_sell_market_button(random.choice([100, 200, 300, 400, 500]))
    ]))
    guiroot.place_buttons()


# buttons creation
dynamicallyaddbuttonbutton = tk.Button(guiroot.frame, text="Add A Button :)",
                                       command=lambda: dynamically_add_buttons())
# guiroot.add_button(dynamicallyaddbuttonbutton)
mktbuy_1 = guiroot.new_buy_market_button(1000)
# addition to root
guiroot.add_button(dynamicallyaddbuttonbutton, mktbuy_1)

# grid placements
guiroot.place_buttons()

# mktbuy_1.grid(row=0, ipadx=5, ipady=5, padx=5, pady=5)

# mktbuy_2.grid(row=1, ipadx=5, ipady=5, padx=5, pady=5)
# limitbuy.grid(row=1, ipadx=5, ipady=5, padx=5, pady=5)
#
# button_s1k.grid(row=0, column=1, ipadx=5, ipady=5, padx=5, pady=5)


async def main():
    om_run = asyncio.create_task(om.run())      # ordermanager loop function
    tk_run = asyncio.create_task(guiroot.run())     # tkinter loop function
    await asyncio.gather(om_run, tk_run)

    # loop = asyncio.get_running_loop()
    # om_result = await loop.run_in_executor(ThreadPoolExecutor(), om.run)
    # gui.mainloop()


if __name__ == '__main__':
    asyncio.run(main())