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


n_ports = serial_ports()
N = len(n_ports)


def add_to_database(*args, ):
    cur.execute(f"""INSERT INTO users({[i for i in n_ports]}) 
                    VALUES('00001', 'Alex', 'Smith', 'male');""")
    bd.commit()


speeds = ['1200', '2400', '4800', '9600', '19200', '38400', '57600', '115200']

