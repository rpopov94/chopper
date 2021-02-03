from serial.tools import list_ports
import time


def serial_ports():
    com_list = []
    ports = list(list_ports.comports())
    for p in ports:
        if "MOXA" in str(p):
            com_list.append(str(p))
    return com_list

while True:
    time.sleep()