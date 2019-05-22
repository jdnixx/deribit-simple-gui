"""
STARTER_LIVE - Main Container

WARNING!!!!!!!!!!!
FOR LIVE USAGE!!
(with deribit_keys_live.txt)

Main module that bootstraps the program.
"""
import asyncio
from utils import log
logger = log.setup_custom_logger(__name__)

logger.info("\n\n Begin")
logger.info("STARTING PROGRAM")

import ordermanager_interface
from tkinter_gui import WindowMarketbuy, tk

INSTRUMENT = 'ETH-PERPETUAL'
# LOOP_INTERVAL = 0.5

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
    # om_run = asyncio.create_task(guiroot.om_run())

    # tk_run = asyncio.create_task(guiroot.run())
    # await asyncio.gather(tk_run)

    # try/except keeps program exit from printing an ugly stacktrace.
    # Also adds a newline to the log on exit
    try:
        await guiroot.run()
    except (KeyboardInterrupt, SystemExit, Exception) as e:
        logger.error(e)
        logger.warning("Program exit with above error.")
        logger.warning("\n")
    finally:
        logger.warning("Program exit.")
        logger.warning("\n")

    # while True:
    #     await pm_run
    #     await tk_run


if __name__ == '__main__':
    logger.info("asyncio.run(main()) STARTED!")
    asyncio.run(main())