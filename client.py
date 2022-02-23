import secrets
import string
import telnetlib

def main():
    host = 'localhost'
    port = 9000
    try:
        tn = telnetlib.Telnet(host, port)
        print('Подключение успешно установлено')
        try:
            for i in range(100):
                bbbb = f'{secrets.randbelow(9999):04}'  # номер участника
                nn = f"C{secrets.choice(string.digits)}"  # id канала
                hh = f'{secrets.randbelow(23):02}'  # Часы
                mm = f'{secrets.randbelow(60):02}'  # минуты
                ss = f'{secrets.randbelow(60):02}'  # секунды
                zhq = f'{secrets.randbelow(1000):03}'  # десятые сотые тысячные
                gg = f'{secrets.randbelow(20):02}'  # номер группы
                message = f'{bbbb} {nn} {hh}:{mm}:{ss}.{zhq} {gg}\n'
                msg = bytes(message, "utf-8")
                tn.write(msg)
        finally:
            print("Работа успешно выполнена!")
            print("Закрываем сокет!")
            tn.close()
    except:
        print("Соединение не уставлено!")
        tn = None



if __name__ == '__main__':
    main()
