import socket
import csv
import json
import requests
from datetime import datetime

def start_my_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('213.189.201.189', 2000))
    server.listen(4)
    print('Working...')
    while True:
        client_socket, address = server.accept()
        data = client_socket.recv(1024).decode('utf-8')
        process_data(data)
        client_socket.send('OK'.encode('utf-8'))
        client_socket.shutdown(socket.SHUT_WR)
    print('Stop')


def process_data(data):
    if len(data.split(' ')) > 1:
        message: str = data.split(' ')[1]
        message = message.split(';')
        msg_time = datetime.now().strftime('%H:%M:%S')
        msg_len = len(message)
        msg_type = message[0]
        msg_from = message[1]

        for i in range(2, msg_len):
            message[i] = message[i].replace('.', ',')

        str_msg = ' '.join(message[2:msg_len+1])
        print('[' + msg_time + ']' + ' From ' + msg_from + ' got message: ' + str_msg)
        message[1] = msg_time
        with open(msg_from + '.csv', mode='a') as file:
            file.write(msg_time + ';' + ';'.join(message[2:msg_len+1])+'\n')

if __name__ == '__main__':
    start_my_server()