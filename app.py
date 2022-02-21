import sys

from PyQt5 import QtWidgets, QtGui
from design import Ui_MainWindow
from calculator import Calculator

class Window(QtWidgets.QMainWindow, Calculator):
  def __init__(self):
    super(Window, self).__init__()
    self.setWindowIcon(QtGui.QIcon("%s/app.ico" % ("/".join(__file__.split("\\")[:-1]))))
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)

    self.label = self.ui.label
    self.operation = 0
    
    self.ui.button1.clicked.connect(self.clearLabel)
    self.ui.button2.clicked.connect(self.root)
    self.ui.button3.clicked.connect(self.backspace)
    self.ui.button4.clicked.connect(self.equal)
    self.ui.button5.clicked.connect(self.printNum("1"))
    self.ui.button6.clicked.connect(self.printNum("2"))
    self.ui.button7.clicked.connect(self.printNum("3"))
    self.ui.button8.clicked.connect(self.divide)
    self.ui.button9.clicked.connect(self.printNum("4"))
    self.ui.button10.clicked.connect(self.printNum("5"))
    self.ui.button11.clicked.connect(self.printNum("6"))
    self.ui.button12.clicked.connect(self.multiply)
    self.ui.button13.clicked.connect(self.printNum("7"))
    self.ui.button14.clicked.connect(self.printNum("8"))
    self.ui.button15.clicked.connect(self.printNum("9"))
    self.ui.button16.clicked.connect(self.subtract)
    self.ui.button17.clicked.connect(self.printNum("0"))
    self.ui.button18.clicked.connect(self.point)
    self.ui.button19.clicked.connect(self.add)
    
app = QtWidgets.QApplication([])
application = Window()
application.show()

sys.exit(app.exec())