import sys
from app.chopper import *
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtCore import QThread
import time

Form, Base = uic.loadUiType("dialog.ui")


class UpdateInterface(QThread):
    req = monitor()
    onebit = req[0]
    twobit = req[1]
    threebit = req[2]
    fourbit = req[3]
    fivebit = req[4]
    sixbit = req[5]
    sevenbit = req[6]
    eightbit = req[7]
    ninebit = req[8]
    tenbit = req[9]
    elevenbit = req[10]
    twentybit = req[11]
    thirtybit = req[12]
    fourteeenbit = req[13]
    fifteenbit = req[14]
    sixteenbit = req[15]
    
    def __init__(self):
        QThread.__init__(self)

    def run(self):
        s = config()
        while True:
            self.req = monitor()
            self.onebit = req[0]
            self.twobit = req[1]
            self.threebit = req[2]
            self.fourbit = req[3]
            self.fivebit = req[4]
            self.sixbit = req[5]
            self.sevenbit = req[6]
            self.eightbit = req[7]
            self.ninebit = req[8]
            self.tenbit = req[9]
            self.elevenbit = req[10]
            self.twentybit = req[11]
            self.thirtybit = req[12]
            self.fourteeenbit = req[13]
            self.fifteenbit = req[14]
            self.sixteenbit = req[15]
            time.sleep(3600)
        
    

class MyWindow(QtWidgets.QWidget, Form):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.current = UpdateInterface()
        self.current.start()
        self.SetData()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.SetData)
        self.timer.start(1000)
        self.pushButton.clicked.connect(self.on_editing)
        self.pushButton_2.clicked.connect(self.monitor_update)
        self.pushButton_5.clicked.connect(self.ch_update_online)
        self.pushButton_11.clicked.connect(self.on_disconnect)
        self.pushButton_12.clicked.connect(self.on_response)
        self.comboBox.addItems(serial_ports())
        
    def SetData(self):
        '''Стереть предыдущее состояние'''
        self.label.setStyleSheet("background-color: #DCDCDC")
        self.label_29.setStyleSheet("background-color: #DCDCDC")
        self.label_45.setStyleSheet("background-color: #DCDCDC")
        self.label_46.setStyleSheet("background-color: #DCDCDC")
        self.label_47.setStyleSheet("background-color: #DCDCDC")
        self.label_48.setStyleSheet("background-color: #DCDCDC")
        self.label_49.setStyleSheet("background-color: #DCDCDC")
        self.label_50.setStyleSheet("background-color: #DCDCDC")
        self.label_51.setStyleSheet("background-color: #DCDCDC")
        self.label_52.setStyleSheet("background-color: #DCDCDC")
        self.label_53.setStyleSheet("background-color: #DCDCDC")
        self.label_54.setStyleSheet("background-color: #DCDCDC")
        self.label_55.setStyleSheet("background-color: #DCDCDC")
        self.label_56.setStyleSheet("background-color: #DCDCDC")
        self.label_57.setStyleSheet("background-color: #DCDCDC")
        self.label_58.setStyleSheet("background-color: #DCDCDC")
        '''реагируем на ответ платы'''
        if self.current.onebit == '1':
            self.label_59.setStyleSheet("background-color: red")
        if self.current.twobit == '1':
            self.label_30.setStyleSheet("background-color: red")
        if self.current.threebit == '1':
            self.label_45.setStyleSheet("background-color: red")
        if self.current.fourbit == '1':
            self.label_46.setStyleSheet("background-color: red")
        if self.current.fivebit == '1':
            self.label_47.setStyleSheet("background-color: red")
        if self.current.sixbit == '1':
            self.label_48.setStyleSheet("background-color: red")
        if self.current.sevenbit == '1':
            self.label_49.setStyleSheet("background-color: red")
        if self.current.eightbit == '1':
            self.label_50.setStyleSheet("background-color: red")
        if self.current.ninebit == '1':
            self.label_51.setStyleSheet("background-color: red")
        if self.current.tenbit == '1':
            self.label_52.setStyleSheet("background-color: red")
        if self.current.elevenbit == '1':
            self.label_53.setStyleSheet("background-color: red")
        if self.current.twentybit == '1':
            self.label_54.setStyleSheet("background-color: red")
        if self.current.thirtybit == '1':
            self.label_55.setStyleSheet("background-color: red")
        if self.current.fourteeenbit == '1':
            self.label_56.setStyleSheet("background-color: red")
        if self.current.fifteenbit == '1':
            self.label_57.setStyleSheet("background-color: red")
        if self.current.sixteenbit == '1':
            self.label_58.setStyleSheet("background-color: red")
        

    def ch_update_online(self):
        response = online_parameters(int(self.plainTextEdit_3.toPlainText()))
        self.label_17.setText(str(response[0]))
        self.label_18.setText(str(response[1]))
        self.label_19.setText(str(response[2]))
        self.label_20.setText(str(response[3]))
        self.label_21.setText(str(response[4]))
        self.label_23.setText(str(response[5]))
        self.label_24.setText(str(response[6]))
        self.label_11.setText(str(response[7]))

    # обновить данные на мониторе
    def monitor_update(self):
        '''обновляем экран, ставим значения по умолчанию'''
        self.label.setStyleSheet("background-color: #DCDCDC")
        self.label_29.setStyleSheet("background-color: #DCDCDC")
        self.label_45.setStyleSheet("background-color: #DCDCDC")
        self.label_46.setStyleSheet("background-color: #DCDCDC")
        self.label_47.setStyleSheet("background-color: #DCDCDC")
        self.label_48.setStyleSheet("background-color: #DCDCDC")
        self.label_49.setStyleSheet("background-color: #DCDCDC")
        self.label_50.setStyleSheet("background-color: #DCDCDC")
        self.label_51.setStyleSheet("background-color: #DCDCDC")
        self.label_52.setStyleSheet("background-color: #DCDCDC")
        self.label_53.setStyleSheet("background-color: #DCDCDC")
        self.label_54.setStyleSheet("background-color: #DCDCDC")
        self.label_55.setStyleSheet("background-color: #DCDCDC")
        self.label_56.setStyleSheet("background-color: #DCDCDC")
        self.label_57.setStyleSheet("background-color: #DCDCDC")
        self.label_58.setStyleSheet("background-color: #DCDCDC")
        '''
         Получаем ответ с конкретного блока и
         формируем статус по нулевому адресу
        '''
        response = ch_update(int(self.plainTextEdit_3.toPlainText()))
        if response[0] == '1':
            self.label_59.setStyleSheet("background-color: red")
        if response[1] == '1':
            self.label_30.setStyleSheet("background-color: red")
        if response[2] == '1':
            self.label_45.setStyleSheet("background-color: red")
        if response[3] == '1':
            self.label_46.setStyleSheet("background-color: red")
        if response[4] == '1':
            self.label_47.setStyleSheet("background-color: red")
        if response[5] == '1':
            self.label_48.setStyleSheet("background-color: red")
        if response[6] == '1':
            self.label_49.setStyleSheet("background-color: red")
        if response[7] == '1':
            self.label_50.setStyleSheet("background-color: red")
        if response[8] == '1':
            self.label_51.setStyleSheet("background-color: red")
        if response[9] == '1':
            self.label_52.setStyleSheet("background-color: red")
        if response[10] == '1':
            self.label_53.setStyleSheet("background-color: red")
        if response[11] == '1':
            self.label_54.setStyleSheet("background-color: red")
        if response[12] == '1':
            self.label_55.setStyleSheet("background-color: red")
        if response[13] == '1':
            self.label_56.setStyleSheet("background-color: red")
        if response[14] == '1':
            self.label_57.setStyleSheet("background-color: red")
        if response[15] == '1':
            self.label_58.setStyleSheet("background-color: red")

    def on_editing(self):
        '''раздел редактирования адреса'''
        ComN = self.comboBox.currentText()
        if ch_connect(ComN):
            self.label_72.setText('Подключено')
            self.label_72.setStyleSheet("background-color: green")
        else:
            self.label_72.setStyleSheet("background-color: red")
            self.label_72.setText('Не удалось подключиться')

    def on_disconnect(self):
        '''отключиться от com порта'''
        ch_disconnect()
        self.label_72.setText('Отключено')
        self.label_72.setStyleSheet("background-color: red")

    def on_response(self):
        '''ответ контроллера'''
        cmd = 'W' if self.checkBox.checkState() else 'R'
        response = smc32_command(int(self.plainTextEdit_2.toPlainText()),
                                 int(self.plainTextEdit_4.toPlainText()),
                                 cmd,
                                 int(self.plainTextEdit.toPlainText()))
        self.plainTextEdit.insertPlainText(str(int(response.decode('utf-8')[11:15], 16)))


if __name__ == "__main__":
    mapp = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(mapp.exec_())
