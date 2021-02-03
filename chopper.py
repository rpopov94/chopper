import serial.tools.list_ports as port_list


def sort_port():
    com_list = []
    ports = list(port_list.comports())
    for p in ports:
        if "MOXA" in str(p):
            com_list.append(p)
    return com_list

s = sort_port()
print(s)