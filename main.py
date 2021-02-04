from chopper import serial_ports, speeds
import serial


class LedApp:
    def __init__(self):
        super().__init__()
        self.realport = None

    def connect(self):
        try:
            self.realport = serial.Serial(self.Port.currentText(), int(self.Speed.currentText()))
            print('Подключено')
        except Exception as e:
            print(e)

    def send(self):
        if self.realport:
            self.realport.write(b'b')


def main():
    window = LedApp()
    app.exec_()


if __name__ == '__main__':
    main()
