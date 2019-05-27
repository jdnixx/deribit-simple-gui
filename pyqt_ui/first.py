# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\first.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(622, 411)
        Form.setAcceptDrops(False)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(520, 370, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 227, 91))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setMaximumSize(QtCore.QSize(60, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setMaxLength(3)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.spinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox.setFont(font)
        self.spinBox.setAutoFillBackground(True)
        self.spinBox.setMaximum(20)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_2.addWidget(self.spinBox)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btn_addMktBuy = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_addMktBuy.setMinimumSize(QtCore.QSize(0, 23))
        self.btn_addMktBuy.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.btn_addMktBuy.setObjectName("btn_addMktBuy")
        self.gridLayout.addWidget(self.btn_addMktBuy, 0, 0, 1, 1)
        self.btn_addMktSell = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_addMktSell.setMinimumSize(QtCore.QSize(0, 23))
        self.btn_addMktSell.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.btn_addMktSell.setObjectName("btn_addMktSell")
        self.gridLayout.addWidget(self.btn_addMktSell, 1, 0, 1, 1)
        self.btn_addLCBuy = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_addLCBuy.setMinimumSize(QtCore.QSize(0, 23))
        self.btn_addLCBuy.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.btn_addLCBuy.setObjectName("btn_addLCBuy")
        self.gridLayout.addWidget(self.btn_addLCBuy, 0, 1, 1, 1)
        self.btn_addLCSell = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_addLCSell.setMinimumSize(QtCore.QSize(0, 23))
        self.btn_addLCSell.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.btn_addLCSell.setObjectName("btn_addLCSell")
        self.gridLayout.addWidget(self.btn_addLCSell, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 120, 160, 241))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.layout_resultbuttons = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.layout_resultbuttons.setContentsMargins(0, 0, 0, 0)
        self.layout_resultbuttons.setObjectName("layout_resultbuttons")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_3.setText(_translate("Form", "PushButton"))
        self.label.setText(_translate("Form", "x 1000 contracts"))
        self.btn_addMktBuy.setText(_translate("Form", "Add Market BUY"))
        self.btn_addMktSell.setText(_translate("Form", "Add Market SELL"))
        self.btn_addLCBuy.setText(_translate("Form", "Add Limit Chase BUY"))
        self.btn_addLCSell.setText(_translate("Form", "Add Limit Chase SELL"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

