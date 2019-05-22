import time
import tkinter as tk

from extras.orders_async import *
from ordermanager_interface import OrderManager
from utils import log

logger = log.setup_custom_logger(__name__)

DEFAULT_INSTRUMENT = 'BTC-PERPETUAL'
LOOP_INTERVAL = 0.020   # ms
#               ^^^^^ 0.020 works well (20ms)
# LOG_LEVEL = logging.DEBUG

# tk.Panel dimensions
HEIGHT = 700
WIDTH = 800



# geom = "%dx%d+%d+%d" % (WIDTH, HEIGHT, 0, -1000)
geom = "%dx%d" % (WIDTH, HEIGHT)

"""
EVENT CALLS
"""
def left_click(event):
    print("left")

# bind leftclick to
# frame.bind("<Button-1>", left_click)

# ACTS AS THE ROOT: i.e. root = tk.Tk()
class WindowMarketbuy(tk.Tk):
    def __init__(self, ordermanager=None):
        if ordermanager:
            self.om = ordermanager
        else:
            self.om = OrderManager(DEFAULT_INSTRUMENT)
        # self.om = __class__.om
        BuySellButton.om = self.om
        Order.om = self.om

        # tk.Tk (root) init
        super().__init__()
        self.geometry(geom)

        # Order.instrument = self.om.instrument
        # Order.client = self.om.client




        ### TKINTER ELEMENTS CREATION ###
        self.frame = tk.Frame(self, bg='lightblue')
        self.frame.place(relwidth=0.5, relheight=0.8, relx=0.1, rely=0.1)

        # self.textbox = tk.Text(self.frame)
        # self.textbox.place(relx=0, rely=0.5, relwidth=0.9, relheight=0.4)

        # create buttons dict
        self.buttons = []

    ### BUTTON METHODS ###
    def place_buttons(self):
        for b in self.buttons:
            b.grid(ipadx=5, ipady=5, padx=5, pady=5)

    def add_button(self, *buttons):
        """add one or multiple Button objects."""
        for b in buttons:
            self.buttons.append(b)

    # button types
    def new_market_button(self, side, amt):
        btn = MarketButton(self.frame, side, amt)
        return btn

    def new_limitchase_button(self, side, amt):
        btn = LimitChaseButton(self.frame, side, amt)
        return btn


    ### RUNTIME METHODS ###
    async def run(self):
        t = time.time()
        while True:
            await self.run_tk()
            # await self.om.run()
            if time.time()-t > 3:       # print every 3 seconds
                logger.info("GUI loop running: @ time {0}".format(time.perf_counter()))
                t = time.time()

    async def run_tk(self):
        """
        Substitutes for root.mainloop() in tkinter. (Makes it async, basically)
        """
        # limitbuy.update_price()

        self.update()
        # print("GUI loop has run: @ time {0}".format(time.perf_counter()))
        await asyncio.sleep(LOOP_INTERVAL)


class BuySellButton(tk.Button):
    om = None
    def __init__(self, master, side, amt):
        super().__init__(master)
        self.side = side
        self.amt = amt
        if side == 'buy':
            # self.config(text="<orderType> Buy %d" % self.amt,
            self.config(None,
                        bg="lightgreen",
                        activebackground="green")
        elif side == 'sell':
            # self.config(text="<orderType> Sell %d" % self.amt,
            self.config(None,
                        bg="firebrick",
                        activebackground="maroon")
        else:
            raise ValueError("'side' parameter must be either 'buy' or 'sell'")
        logger.info(f"{side.upper()} Button created, amt={amt}...with master={master}")

class MarketButton(BuySellButton):
    def __init__(self, master, side, amt):
        super().__init__(master, side, amt)
        self.config(text=f"Market {self.side} {self.amt}",
                    command=lambda : self._make())

    def _make(self):
        ordertask = asyncio.create_task(self.om.market_order(self.side, self.amt))
        logger.info(f"Market button ordertask created: {ordertask}")

class LimitChaseButton(BuySellButton):
    def __init__(self, master, side, amt):
        super().__init__(master, side, amt)
        self.config(text=f"Limit CHASE {self.side} {self.amt}",
                    command=lambda : self._make())

    def _make(self):
        ordertask = asyncio.create_task(self.om.limit_chase(self.side, self.amt))
        logger.info(f"LimitChase button ordertask created: {ordertask}")