from serial.tools import list_ports, miniterm
import sqlite3

bd = sqlite3.connect("chopper.sqllite")

cur = bd.cursor()


def create_table(columm):
    cur.execute('''
                create table if not exists chopper(
                id INT PRIMARY KEY
                );

                ''')
    for col in columm:
        cur.execute("alter table chopper add column '%s' 'string'" % col)
    bd.commit()


def serial_ports():
    com_list = []
    ports = list(list_ports.comports())
    for p in ports:
        if "MOXA" in str(p):
            com_list.append(str(p)[:4])
    return com_list


columm = serial_ports()
create_table(columm)
