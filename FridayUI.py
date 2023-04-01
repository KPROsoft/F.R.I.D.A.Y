# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FridayUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class UiFriday:
    """Program gui class"""

    def __init__(self):
        self.pushButton_2 = None
        self.pushButton = None
        self.label = None
        self.centralwidget = None

    def setup(self, friday):
        """Setting up button sizes and text"""
        friday.setObjectName("friday")
        friday.resize(797, 581)
        friday.setMinimumSize(QtCore.QSize(0, 0))
        friday.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon.fromTheme("VA")
        friday.setWindowIcon(icon)
        friday.setAutoFillBackground(True)
        friday.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.centralwidget = QtWidgets.QWidget(friday)
        self.centralwidget.setObjectName("central-widget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 581))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("untitled-6.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(540, 510, 93, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setAutoExclusive(False)
        self.pushButton.setDefault(True)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(650, 510, 93, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 59, 0);")
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setDefault(True)
        self.pushButton_2.setObjectName("pushButton_2")
        friday.setCentralWidget(self.centralwidget)

        self.translate(friday)
        QtCore.QMetaObject.connectSlotsByName(friday)

    def translate(self, friday):
        """Setting up icon and buttons"""
        _translate = QtCore.QCoreApplication.translate
        friday.setWindowTitle(_translate("friday", "FRIDAY"))
        friday.setWindowIcon(QtGui.QIcon("icon.ico"))
        self.pushButton.setText(_translate("friday", "INITIALIZE"))
        self.pushButton_2.setText(_translate("friday", "TERMINATE"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    friday = QtWidgets.QMainWindow()
    ui = UiFriday()
    ui.setup(friday)
    friday.show()
    sys.exit(app.exec_())
