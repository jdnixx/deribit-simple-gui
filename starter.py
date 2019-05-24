"""
STARTER - Main Container

Main module that bootstraps the program.

*currently used for testing, mostly*
I'm experimenting with GUI changes, so this separates the bot startup from the Tkinter window
"""
import asyncio
from utils import log
logger = log.setup_custom_logger(__name__)

logger.info("\n\n Begin")
logger.info("STARTING PROGRAM")

import ordermanager_interface
from tkinter_gui import WindowMarketbuy, tk

INSTRUMENT_BTC = 'BTC-PERPETUAL'
INSTRUMENT_ETH = 'ETH-PERPETUAL'
# LOOP_INTERVAL = 0.5

client = ordermanager_interface.NewClient('../deribit_keys.txt')
omBTC = omETH = guirootBTC = guirootETH = None

omBTC = ordermanager_interface.OrderManager(INSTRUMENT_BTC, client)
guirootBTC = WindowMarketbuy(omBTC)
# omETH = ordermanager_interface.OrderManager(INSTRUMENT, client)
# guirootETH = WindowMarketbuy(omETH)



"""
TKINTER SETUP
"""

### "ADD BUTTON" BUTTON ###
# 'amount' entry box
addbtn_entry = tk.Entry(guirootBTC.frame, exportselection=0)

# button creation & placement
def dynamically_add_buttons_market(side):
    guirootBTC.add_button(guirootBTC.new_market_button(side, addbtn_entry.get()))
    guirootBTC.place_buttons()
def dynamically_add_buttons_limitchase(side):
    guirootBTC.add_button(guirootBTC.new_limitchase_button(side, addbtn_entry.get()))
    guirootBTC.place_buttons()
# def dynamically_add_buttons():
#     guiroot.add_button(random.choice([
#         guiroot.new_buy_market_button(random.choice([100, 200, 300, 400, 500])),
#         guiroot.new_sell_market_button(random.choice([100, 200, 300, 400, 500]))
#     ]))
#     guiroot.place_buttons()


dynamicallyaddbutton_limitchase_buy = tk.Button(guirootBTC.frame, text="Add :) LimitChase BUY",
                                           command=lambda : dynamically_add_buttons_limitchase('buy'))
dynamicallyaddbutton_limitchase_sell = tk.Button(guirootBTC.frame, text="Add :) LimitChase SELL",
                                           command=lambda : dynamically_add_buttons_limitchase('sell'))
dynamicallyaddbutton_market_buy = tk.Button(guirootBTC.frame, text="Add :) Market BUY",
                                           command=lambda : dynamically_add_buttons_market('buy'))
dynamicallyaddbutton_market_sell = tk.Button(guirootBTC.frame, text="Add :) Market SELL",
                                           command=lambda : dynamically_add_buttons_market('sell'))





mktbuy_1 = guirootBTC.new_market_button('buy', 10)
limitchase_1 = guirootBTC.new_limitchase_button('buy', 50)
limitch_sell_1 = guirootBTC.new_limitchase_button('sell', 50)
guirootBTC.add_button(dynamicallyaddbutton_limitchase_buy, dynamicallyaddbutton_limitchase_sell,
                      dynamicallyaddbutton_market_buy, dynamicallyaddbutton_market_sell,
                      mktbuy_1, limitchase_1, limitch_sell_1)
guirootBTC.place_buttons()


addbtn_entry.grid(row=0, column=1)

# mktbuy_1.grid(row=0, ipadx=5, ipady=5, padx=5, pady=5)

# mktbuy_2.grid(row=1, ipadx=5, ipady=5, padx=5, pady=5)
# limitbuy.grid(row=1, ipadx=5, ipady=5, padx=5, pady=5)
#
# button_s1k.grid(row=0, column=1, ipadx=5, ipady=5, padx=5, pady=5)


async def main():
    # try/except keeps program exit from printing an ugly stacktrace.
    # Also adds a newline to the log on exit
    try:
        if omBTC and guirootBTC:
            await guirootBTC.run()
        if omETH and guirootETH:
            await guirootETH.run()
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