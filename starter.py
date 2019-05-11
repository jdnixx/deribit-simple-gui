"""
STARTER - Main Container

Main module that bootstraps the program.

*currently used for testing, mostly*
I'm experimenting with GUI changes, so this separates the bot startup from the Tkinter window
"""
import time
import asyncio
from concurrent.futures import ThreadPoolExecutor

from extras.position_monitor import Monitor
from ordermanager_interface import OrderManager
from tkinter_gui import WindowMarketbuy, tk

import random

"""
INITIAL DECLARATIONS
"""
INSTRUMENT = 'BTC-PERPETUAL'
LOOP_INTERVAL = 0.5


# OrderManager instance
om = OrderManager(INSTRUMENT)

# assign same om object across all Monitor and Window instances
Monitor.om = om
WindowMarketbuy.om = om

pm = Monitor()
guiroot = WindowMarketbuy()


### TKINTER SETUP ###

# "Add Button" button; purely for testing
def dynamically_add_buttons():
    guiroot.add_button(random.choice([
        guiroot.new_buy_market_button(random.choice([100, 200, 300, 400, 500])),
        guiroot.new_sell_market_button(random.choice([100, 200, 300, 400, 500]))
    ]))
    guiroot.place_buttons()


dynamicallyaddbuttonbutton = tk.Button(guiroot.frame, text="Add A Button :)",
                                       command=lambda: dynamically_add_buttons())
mktbuy_1 = guiroot.new_buy_market_button(1000)
guiroot.add_button(dynamicallyaddbuttonbutton, mktbuy_1)
guiroot.place_buttons()

# mktbuy_1.grid(row=0, ipadx=5, ipady=5, padx=5, pady=5)

# mktbuy_2.grid(row=1, ipadx=5, ipady=5, padx=5, pady=5)
# limitbuy.grid(row=1, ipadx=5, ipady=5, padx=5, pady=5)
#
# button_s1k.grid(row=0, column=1, ipadx=5, ipady=5, padx=5, pady=5)


async def main():
    om_run = asyncio.create_task(om.run())
    pm_run = asyncio.create_task(pm.run())
    tk_run = asyncio.create_task(guiroot.run())
    await asyncio.gather(om_run, tk_run)
    print("blerp!!")
    await asyncio.sleep(3)

    # while True:
    #     await pm_run
    #     await tk_run


if __name__ == '__main__':
    asyncio.run(main())