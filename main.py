import sys
from serial import *
from PyQt5 import QtCore, QtGui, QtWidgets
from chopper_ui import Ui_CHOPPER
from chopper import ch_connect


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_CHOPPER()
        self.ui.setupUi(self)

        # подключение клик-сигнал к слоту btnClicked
        self.ui.pushButton.clicked.connect(self.btnClicked)

    def btnClicked(self):
        print('press send')
        com = self.ui.comboBox.currentText()
        ch_connect(com)
        # self.ui.plainTextEdit_3.appendPlainText('btnClicked')
        # t = self.ui.plainTextEdit_3.toPlainText()
        # print(t)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = mywindow()
    myapp.show()
    sys.exit(app.exec_())