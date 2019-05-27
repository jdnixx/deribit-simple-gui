import asyncio
import sys
from asyncqt import QEventLoop

from pyqt_ui import first

def run_qtui():
    app = first.QtWidgets.QApplication([])
    loop = QEventLoop(app)
    return loop

def create():
    Form = first.QtWidgets.QWidget()
    ui = first.Ui_Form()
    ui.setupUi(Form)

    Form.show()
    # app.exec_()


class AsyncQt:
    def __init__(self):
        self.app = first.QtWidgets.QApplication([])
        self.Form = first.QtWidgets.QWidget()
        self.ui = first.Ui_Form()
        self.ui.setupUi(self.Form)

        self.Form.show()

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
