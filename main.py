import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from chopper_ui import *


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_CHOPPER()
        self.ui.setupUi(self)
        '''
        add new elements
        '''
        self.ui.comboBox.addItem('COM1')
        self.ui.comboBox.addItem('COM2')
        self.ui.comboBox.addItem('COM3')
        self.ui.comboBox.addItem('COM4')
        self.ui.comboBox.addItem('COM5')
        self.ui.comboBox.addItem('COM6')
        self.ui.comboBox.addItem('COM7')
        self.ui.comboBox.addItem('COM8')
        self.ui.comboBox.addItem('COM9')
        self.ui.comboBox.addItem('COM10')
        self.ui.comboBox.addItem('COM12')
        self.ui.comboBox.addItem('COM13')
        self.ui.comboBox.addItem('COM14')
        self.ui.comboBox.addItem('COM15')
        self.ui.comboBox.addItem('COM16')
        self.ui.comboBox.addItem('COM17')
        self.ui.comboBox.addItem('COM18')
        self.ui.comboBox.addItem('COM19')
        self.ui.comboBox.addItem('COM20')
        self.ui.comboBox.addItem('COM21')
        self.ui.comboBox.addItem('COM22')
        self.ui.comboBox.addItem('COM23')
        self.ui.comboBox.addItem('COM24')
        self.ui.comboBox.addItem('COM25')
        self.ui.comboBox.addItem('COM26')
        self.ui.comboBox.addItem('COM27')
        self.ui.comboBox.addItem('COM28')
        self.ui.comboBox.addItem('COM29')
        self.ui.comboBox.addItem('COM30')
        self.ui.comboBox.addItem('COM31')
        self.ui.comboBox.addItem('COM32')
        self.ui.comboBox.addItem('COM33')
        self.ui.comboBox.addItem('COM34')
        self.ui.comboBox.addItem('COM35')
        self.ui.comboBox.addItem('COM36')
        self.ui.comboBox.addItem('COM37')
        self.ui.comboBox.addItem('COM38')
        self.ui.comboBox.addItem('COM39')
        self.ui.comboBox.addItem('COM40')
        self.ui.comboBox.addItem('COM41')
        self.ui.comboBox.addItem('COM42')
        self.ui.comboBox.addItem('COM43')
        self.ui.comboBox.addItem('COM44')
        self.ui.comboBox.addItem('COM45')
        self.ui.comboBox.addItem('COM46')
        self.ui.comboBox.addItem('COM47')
        self.ui.comboBox.addItem('COM48')
        self.ui.comboBox.addItem('COM49')
        self.ui.comboBox.addItem('COM50')



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())