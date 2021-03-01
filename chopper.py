from serial import *
from serial.tools import list_ports


def serial_ports():
    """
    данные о подключенных портах
    """
    com_list = []
    ports = list(list_ports.comports())
    for p in ports:
        if "MOXA" in str(p):
            com_list.append(str(p)[:4])
    print("Подлюченные устройства:")
    print(*com_list, sep="\n")
    if len(com_list) == 0:
        return 'Нет подключенных устройств'
    else:
        return com_list


def connect(name):
    '''
    :param name: имя порта
    :return: возвращает статус подкючения
    '''
    name = name.upper()
    global ser
    ser = Serial(
        port=name,
        baudrate=9600,
        bytesize=8,
        parity='N',
        stopbits=2,
        timeout=1,
        writeTimeout=1
    )
    try:
        ser.isOpen()
        return 'Succsesful!'
    except Exception as e:
        return f'Serial port {ser.name} {e}'


def smc32_command(nblock, register, cmd, data):
    """
    :param nblock: номер блока
    :param register: номер регистра
    :param cmd: команда чтения/запись
    :param data: слово состояния
    """
    mode = ''
    STX = '%c' % 2
    HSC = '%c' % 0x7c
    bl = '%02x' % nblock
    Reg = '%03x' % register
    if cmd.upper() == 'R':
        mode = '%c' % 0x52
    elif cmd.upper() == 'W':
        mode = '%c' % 0x57
    ENQ = '%c' % 5
    DATA = '%04x' % data
    ETX = '%c' % 3
    request = f'{STX}{HSC}{bl}{HSC}{Reg}{HSC}{mode}{HSC}{DATA}{HSC}{ENQ}{HSC}{ETX}'.encode('utf-8')
    print('Request is:  ', request)
    ser.write(request)


def smc32response():
    """
    :return: ответ блока на запрос
    """
    response = ser.readline()
    ser.close()
    print('Response is: ', response)
    return response


def get_command(string):
    """
    :param string: команда блоку
    :return: возвращает ответ
    """
    myrequest = string.split(',')
    nblock, register, cmd, data = myrequest
    generate_command(int(nblock), int(register), cmd, int(data))
    reply = myresponse().decode('utf-8')[2:-4]
    reply = reply.split('|')
    return f'reply = |{int(reply[0], 16)}|' \
           f'{int(reply[1], 16)}|' \
           f'{reply[2]}|' \
           f'{int(reply[3], 16)}|'


def smart_function(string):
    if "COM" in string.upper():
        return my_connect(string)
    elif ',' in string:
        return get_command(string)