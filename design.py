# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(295, 340)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(11, 0, 279, 51))
        self.label.setStyleSheet(
            "background: rgb(220, 220, 220);\n"
            "border: 1px solid rgb(180, 180, 180);\n"
            "font: 18px Arial\n")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.button12 = QtWidgets.QPushButton(self.centralwidget)
        self.button12.setGeometry(QtCore.QRect(220, 150, 71, 51))
        self.button12.setObjectName("button12")
        self.button8 = QtWidgets.QPushButton(self.centralwidget)
        self.button8.setGeometry(QtCore.QRect(220, 100, 71, 51))
        self.button8.setObjectName("button8")
        self.button3 = QtWidgets.QPushButton(self.centralwidget)
        self.button3.setGeometry(QtCore.QRect(150, 50, 71, 51))
        self.button3.setObjectName("button3")
        self.button19 = QtWidgets.QPushButton(self.centralwidget)
        self.button19.setGeometry(QtCore.QRect(220, 250, 71, 51))
        self.button19.setObjectName("button19")
        self.button16 = QtWidgets.QPushButton(self.centralwidget)
        self.button16.setGeometry(QtCore.QRect(220, 200, 71, 51))
        self.button16.setObjectName("button16")
        self.button4 = QtWidgets.QPushButton(self.centralwidget)
        self.button4.setGeometry(QtCore.QRect(220, 50, 71, 51))
        self.button4.setObjectName("button4")
        self.button5 = QtWidgets.QPushButton(self.centralwidget)
        self.button5.setGeometry(QtCore.QRect(10, 100, 71, 51))
        self.button5.setObjectName("button5")
        self.button6 = QtWidgets.QPushButton(self.centralwidget)
        self.button6.setGeometry(QtCore.QRect(80, 100, 71, 51))
        self.button6.setObjectName("button6")
        self.button7 = QtWidgets.QPushButton(self.centralwidget)
        self.button7.setGeometry(QtCore.QRect(150, 100, 71, 51))
        self.button7.setObjectName("button7")
        self.button9 = QtWidgets.QPushButton(self.centralwidget)
        self.button9.setGeometry(QtCore.QRect(10, 150, 71, 51))
        self.button9.setObjectName("button9")
        self.button10 = QtWidgets.QPushButton(self.centralwidget)
        self.button10.setGeometry(QtCore.QRect(80, 150, 71, 51))
        self.button10.setObjectName("button10")
        self.button11 = QtWidgets.QPushButton(self.centralwidget)
        self.button11.setGeometry(QtCore.QRect(150, 150, 71, 51))
        self.button11.setObjectName("button11")
        self.button13 = QtWidgets.QPushButton(self.centralwidget)
        self.button13.setGeometry(QtCore.QRect(10, 200, 71, 51))
        self.button13.setObjectName("button13")
        self.button14 = QtWidgets.QPushButton(self.centralwidget)
        self.button14.setGeometry(QtCore.QRect(80, 200, 71, 51))
        self.button14.setObjectName("button14")
        self.button15 = QtWidgets.QPushButton(self.centralwidget)
        self.button15.setGeometry(QtCore.QRect(150, 200, 71, 51))
        self.button15.setObjectName("button15")
        self.button17 = QtWidgets.QPushButton(self.centralwidget)
        self.button17.setGeometry(QtCore.QRect(10, 250, 141, 51))
        self.button17.setObjectName("button17")
        self.button18 = QtWidgets.QPushButton(self.centralwidget)
        self.button18.setGeometry(QtCore.QRect(150, 250, 71, 51))
        self.button18.setObjectName("button18")
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(10, 50, 71, 51))
        self.button1.setObjectName("button1")
        self.button2 = QtWidgets.QPushButton(self.centralwidget)
        self.button2.setGeometry(QtCore.QRect(80, 50, 71, 51))
        self.button2.setObjectName("button2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 295, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор"))
        self.button12.setText(_translate("MainWindow", "*"))
        self.button8.setText(_translate("MainWindow", "/"))
        self.button3.setText(_translate("MainWindow", "←"))
        self.button19.setText(_translate("MainWindow", "+"))
        self.button16.setText(_translate("MainWindow", "-"))
        self.button4.setText(_translate("MainWindow", "="))
        self.button5.setText(_translate("MainWindow", "1"))
        self.button6.setText(_translate("MainWindow", "2"))
        self.button7.setText(_translate("MainWindow", "3"))
        self.button9.setText(_translate("MainWindow", "4"))
        self.button10.setText(_translate("MainWindow", "5"))
        self.button11.setText(_translate("MainWindow", "6"))
        self.button13.setText(_translate("MainWindow", "7"))
        self.button14.setText(_translate("MainWindow", "8"))
        self.button15.setText(_translate("MainWindow", "9"))
        self.button17.setText(_translate("MainWindow", "0"))
        self.button18.setText(_translate("MainWindow", "."))
        self.button1.setText(_translate("MainWindow", "C"))
        self.button2.setText(_translate("MainWindow", "√"))