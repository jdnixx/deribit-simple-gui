import asyncio
from asyncqt import QEventLoop
from PyQt5 import QtWidgets

from pyqt_ui.first import Ui_Form
from ordermanager_interface import OrderManager
from utils import log

logger = log.setup_custom_logger(__name__)


class FinalGUI(QtWidgets.QWidget):
    def __init__(self, ordermanager=None):
        super().__init__()
        self.om = ordermanager or OrderManager()
        OrderButton.om = self.om
        self.ui = Ui_Form()     # these lines are
        self.ui.setupUi(self)   # from Ui_Form class
        # self.spawnedbuttons = []

    def get_amt(self):
        amt = self.ui.spinBox.value() * 1000
        if self.ui.lineEdit.text() is not "":
            amt = self.ui.lineEdit.text()
        return amt

    def add_mktbuy_btn(self):
        btn = MarketButton(self, 'buy', self.get_amt())
        self.ui.layout_spawnedbuttons.addWidget(btn)

    def add_mktsell_btn(self):
        btn = MarketButton(self, 'sell', self.get_amt())
        self.ui.layout_spawnedbuttons.addWidget(btn)

    def add_limitchasebuy_btn(self):
        btn = LimitChaseButton(self, 'buy', self.get_amt())
        self.ui.layout_spawnedbuttons.addWidget(btn)

    def add_limitchasesell_btn(self):
        btn = LimitChaseButton(self, 'sell', self.get_amt())
        self.ui.layout_spawnedbuttons.addWidget(btn)


    def lineEdit_amt_edited(self):
        pass




class AsyncQt:
    def __init__(self, om=None):
        self.app = QtWidgets.QApplication([])
        self.gui = FinalGUI(om)
        self.gui.show()
        # app.exec_()

    async def run_asyncqt(self):
        # ctr = 0
        while True:
            # print(ctr)
            # ctr += 1
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

class OrderButton(QtWidgets.QPushButton):
    om = None
    def __init__(self, master, side, amt):
        super().__init__(master)
        if side == 'buy':
            pass
        elif side == 'sell':
            pass
        else:
            raise ValueError("'side' parameter must be either 'buy' or 'sell'")
        self.side = side
        self.amt = amt
        self.setText(f"{self.ordertype} {self.side} {self.amt}")
        logger.info(f"{self.ordertype} {self.side.upper()} Button created, amt={self.amt}...with master={master}")

class LimitChaseButton(OrderButton):
    def __init__(self, master, side, amt):
        self.ordertype = 'LimitChase'
        super().__init__(master, side, amt)
        self.setObjectName(f"new_button_limitchase_{self.side}")
        # self.btn_addMktBuy.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.clicked.connect(lambda : asyncio.create_task(self.om.limit_chase(self.side, self.amt)))
        logger.info(f"LimitChase button ordertask initialized")
        # logger.info(f"Market button ordertask created: {ordertask}")

class MarketButton(OrderButton):
    def __init__(self, master, side, amt):
        self.ordertype = 'Market'
        super().__init__(master, side, amt)
        self.setObjectName(f"new_button_market_{self.side}")
        # self.btn_addMktBuy.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.clicked.connect(lambda : asyncio.create_task(self.om.market_order(self.side, self.amt)))
        logger.info(f"Market button ordertask initialized")
        # logger.info(f"Market button ordertask created: {ordertask}")
