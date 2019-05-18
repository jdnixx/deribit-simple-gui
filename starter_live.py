"""
STARTER - Main Container

Main module that bootstraps the program.

*currently used for testing, mostly*
I'm experimenting with GUI changes, so this separates the bot startup from the Tkinter window
"""
import asyncio

import ordermanager_interface
from tkinter_gui import WindowMarketbuy, tk

import random

"""
INITIAL DECLARATIONS
"""
INSTRUMENT = 'ETH-PERPETUAL'
# LOOP_INTERVAL = 0.5


# OrderManager instance
# om = OrderManager(INSTRUMENT)

# assign same om object across all Monitor and Window instances
# Monitor.om = om
# WindowMarketbuy.om = om

# pm = Monitor()
client = ordermanager_interface.NewClient('../deribit_keys_live.txt')
om = ordermanager_interface.OrderManager(INSTRUMENT, client)
guiroot = WindowMarketbuy(om)


"""
TKINTER SETUP
"""

### "ADD BUTTON" BUTTON ###
# 'amount' entry box
addbtn_entry = tk.Entry(guiroot.frame, exportselection=0)

# button creation & placement
def dynamically_add_buttons():
    guiroot.add_button(guiroot.new_limitchase_button('buy', addbtn_entry.get()))
    guiroot.place_buttons()
# def dynamically_add_buttons():
#     guiroot.add_button(random.choice([
#         guiroot.new_buy_market_button(random.choice([100, 200, 300, 400, 500])),
#         guiroot.new_sell_market_button(random.choice([100, 200, 300, 400, 500]))
#     ]))
#     guiroot.place_buttons()


dynamicallyaddbuttonbutton = tk.Button(guiroot.frame, text="Add A Button :)",
                                       command=lambda : dynamically_add_buttons())





mktbuy_1 = guiroot.new_market_button('buy', 10)
limitchase_1 = guiroot.new_limitchase_button('buy', 500)
limitch_sell_1 = guiroot.new_limitchase_button('sell', 510)
guiroot.add_button(dynamicallyaddbuttonbutton, mktbuy_1, limitchase_1, limitch_sell_1)
guiroot.place_buttons()


addbtn_entry.grid(row=0, column=1)

# mktbuy_1.grid(row=0, ipadx=5, ipady=5, padx=5, pady=5)

# mktbuy_2.grid(row=1, ipadx=5, ipady=5, padx=5, pady=5)
# limitbuy.grid(row=1, ipadx=5, ipady=5, padx=5, pady=5)
#
# button_s1k.grid(row=0, column=1, ipadx=5, ipady=5, padx=5, pady=5)


async def main():
    tk_run = asyncio.create_task(guiroot.run())
    # om_run = asyncio.create_task(guiroot.om_run())
    await asyncio.gather(tk_run)

    # while True:
    #     await pm_run
    #     await tk_run


if __name__ == '__main__':
    asyncio.run(main())