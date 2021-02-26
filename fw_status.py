class Status:
    def __init__(self, response):
        self.response = response

    def get_status(self, string):
        message = []
        d = {
            0: "тумблер на передней панели",
            1: "Получена останов прерывателя",
            2: "система сама  прекратила попытки стабилизации\nи сняла напряжение с двигателя",
            3: "блокировка работы блока С ПЕРЕДНЕЙ ПАНЕЛИ",
            4: "программа стабилизации периода",
            5: "период стабильно в заданном диапазоне",
            6: "селекторных импульсов нет либо они не появились\n"
               "устанавливается в ISR_T1 при превышении количества "
               "реперов\nявляется .только индикацией совместно с битом 2",
            7: "ловушка первого входа в  стабилизацию периода селектора Tс",
            8: "период селектора Тс в заданном диапазоне (контроль точности)",
            9: "программа стабилизации фазы",
            10: "фаза   стабильно в заданном диапазоне",
            11: "ловушка первого входа в  стабилизацию фазы  F",
            12: "флаг - F в заданном диапазоне (контроль точности)",
            13: "флаг - период стартов в заданных пределах",
            14: "зарегистрирована одна из целого комплекса ошибок:\n"
                "выход  фазы из диапазона\nвыход  из фазы в период\n"
                "при резком изменении фазы\n!VFL-VFN!>200mkc",
            15: "неверное задание",
        }
        for key in string:
            message.append(d[key])
        return message

    def get_response(self):
        b = list(str(bin(self.response))[2::])
        p = [int(i) for i in b][::-1]
        resp = []
        for k in range(len(p)):
            if p[k] != 0:
                resp.append(k)
        print(*resp)
        return resp


st = Status(68)
r = st.get_response()
print(st.get_status(r))
