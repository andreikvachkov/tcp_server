import re
import socket
import logging

def main():
    host = 'localhost'
    port = 9000

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаем сокет
    sock.bind((host, port)) # привязываем сокет к порту

    sock.listen(1) # слушаем входящее подключение

    logging.basicConfig(filename="sample.log", level=logging.INFO) # создание лога
    logger = logging.getLogger('server')
    logger.setLevel(logging.INFO)

    msg = ''
    while True:
        print('Ожидание соединения...')
        connection, client_address = sock.accept()
        print('Подключение к:', client_address)
        try:
            while True:
                data = connection.recv(4096).decode('utf-8')
                if data:
                    records = f'{msg}{data}'.split('\n')
                    for record in records:
                        if len(record) == 23:
                            bbbb, nn, hh, mm, ss_zsh, gg = re.split(' |:', record)
                            if gg == '00':
                                print(f'Спортсмен, нагрудный номер {bbbb} прошёл отсечку {nn} в «{hh}:{mm}:{ss_zsh[:4]}»')
                            else:
                                logging.info(record)
                        else:
                            msg = record
                else:
                    break
        except ValueError:
            connection.close()
            logging.info('ValueError! Connection close!!!')

if __name__ == '__main__':
    main()




