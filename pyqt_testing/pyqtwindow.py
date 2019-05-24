from PyQt5 import QtWidgets as qwid

from extras.orders_async import *
from ordermanager_interface import OrderManager

from utils import log


# Constants
DEFAULT_INSTRUMENT = 'BTC-PERPETUAL'

# Logging
logger = log.setup_custom_logger(__name__)


class Window(qwid.QMainWindow):
    def __init__(self, ordermanager=None):
        # OrderManager setup process
        self.om = ordermanager
        if not ordermanager:
            self.om = OrderManager() # by default uses 'BTC-PERPETUAL' as instrument
        Order.om = self.om
        # BuySellButton.om = self.om # TODO

        # window init call
        super().__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle('PyQt boiiiiiiiii')

        self.create_button()




        self.show()

    def create_button(self):
        self.button = qwid.QPushButton("First Butt on", self)

        self.button.clicked.connect(self.go)


        # button.show()
        # button2.show()
        # button3.show()

    def go(self):
        self.button.setText("CHANGEDDDDD")
        print("blerp")


app = qwid.QApplication([])
omlol = OrderManager(path_to_keyfile='../../deribit_keys.txt') # TODO: DELETE LOL
win = Window(omlol)




app.exec_()