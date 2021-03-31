import serial
import sys
import glob


def serial_ports():
    """ Lists serial port names
        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


# ser = serial.Serial()
global ser


def ch_connect(name):
    global ser
    ser = serial.Serial(
        port=name.upper(),
        baudrate=9600,
        bytesize=8,
        parity='N',
        stopbits=2,
        timeout=1,
        writeTimeout=1,
    )

    if ser.isOpen():
        return True
    else:
        return False


def ch_disconnect():
    ser.close()


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
    request = f'{STX}{HSC}{bl}{HSC}{Reg}{HSC}{mode}{HSC}' \
              f'{DATA}{HSC}{ENQ}{HSC}{ETX}'.encode('utf-8')
    # print('Request is:  ', request)
    ser.write(request)
    return ser.readline()


def config():
    conf = {}
    s = []
    with open('config.txt', 'r') as f:
        nums = f.read().splitlines()
    for n in nums:
        s.append(n.split(':'))
    for i in range(len(s)):
        conf[s[i][0]] = s[i][1]
    return conf

print(config())

def monitor():
    s = config()
    for i in s:
        ch_connect(str(s[i][0]))
        response = smc32_command(int(s[i][1]), 0, 'r', 0)
        response = response.decode('utf-8')[11:15]
        response = list(str(bin(int(response, 16))[2:]))
        ch_disconnect()

def smc32response():
    """
    :return: ответ блока на запрос
    """
    response = ser.readline()
    ser.close()
    print('Response is: ', response)
    return response


def ch_update(block):
    response = smc32_command(block, 0, 'R', 0)
    response = response.decode('utf-8')[11:15]
    response = list(str(bin(int(response, 16))[2:]))
    if len(response) < 16:
        l = 16 - len(response)
        for i in range(l):
            response.insert(i, 0)
    return response[::-1]


def online_parameters(block):
    '''функция опроса онлайн параметров'''
    params = [1, 2, 3, 4, 344, 234, 236, 345]
    req = []
    for p in params:
        response = smc32_command(block, p, 'R', 0)
        response = response.decode('utf-8')[11:15]
        req.append(int(response, 16))
    return req

def get_command(string):
    """
    :param string: команда блоку
    :return: возвращает ответ
    """
    myrequest = string.split(',')
    nblock, register, cmd, data = myrequest
    smc32_command(int(nblock), int(register), cmd, int(data))
    reply = smc32response().decode('utf-8')[2:-4]
    reply = reply.split('|')
    return f'reply = |{int(reply[0], 16)}|' \
           f'{int(reply[1], 16)}|' \
           f'{reply[2]}|' \
           f'{int(reply[3], 16)}|'


def smart_function(string):
    if "COM" in string.upper():
        return ch_connect(string)
    elif ',' in string:
        return get_command(string)
