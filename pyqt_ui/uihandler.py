import asyncio
from asyncqt import QEventLoop
from PyQt5 import QtWidgets

from pyqt_ui.first import Ui_Form
from ordermanager_interface import OrderManager
from utils import log

logger = log.setup_custom_logger(__name__)


class BuySellButton(QtWidgets.QPushButton):
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


class FinalGUI(QtWidgets.QWidget):
    def __init__(self, ordermanager=None):
        super().__init__()
        self.om = ordermanager or OrderManager()
        self.ui = Ui_Form()     # these lines are
        self.ui.setupUi(self)   # from Ui_Form class
        # self.spawnedbuttons = []

    def add_mktbuy_btn(self):
        btn = QtWidgets.QPushButton(self)
        btn.setObjectName("new_button_market_buy")
        # self.btn_addMktBuy.setStyleSheet("background-color: rgb(0, 255, 0);")

        amt = self.ui.spinBox.value() * 1000
        if self.ui.lineEdit.text() is not "":
            amt = self.ui.lineEdit.text()
            print(amt)
        btn.clicked.connect(lambda : asyncio.create_task(self.om.market_order('buy', amt)))

        btn.setText(f"Market buy {amt}")
        self.ui.layout_spawnedbuttons.addWidget(btn)

    def add_mkt_sell(self):
        btn = MarketButton(None, 'sell', self.get_amt())
        self.ui.layout_spawnedbuttons.addWidget(btn)


    def lineEdit_amt_edited(self):
        pass

    # def add_mktbuy_btn(self):



class AsyncQt:
    def __init__(self, om=None):
        self.app = QtWidgets.QApplication([])
        self.gui = FinalGUI(om)
        self.gui.show()
        # app.exec_()

    async def run_asyncqt(self):
        ctr = 0
        while True:
            print(ctr)
            ctr += 1
            self.app.processEvents()
            await asyncio.sleep(0.02)


# print(asyncio.get_event_loop())
# app = first.QtWidgets.QApplication([])
# loop = QEventLoop(app)
# asyncio.set_event_loop(loop)
# print(asyncio.get_event_loop())
# Form = first.QtWidgets.QWidget()
# ui = first.Ui_Form()
# ui.setupUi(Form)
# Form.show()
#
#
#
# with loop:
#     print(asyncio.get_event_loop())
#     loop.create_task(asyncio.sleep(3))
#     sys.exit(loop.run_forever())
