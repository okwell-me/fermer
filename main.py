import socket
import csv

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
    print(data.split(' ')[1])
    if len(data.split(' ')) > 1:
        message = data.split(' ')[1]
        message = message.split(';')
        msg_count = len(message)
        msg_type = message[0]
        print('message type: ')
        if msg_type == '/DAT':
            print('data')
        if msg_type == '/SYS':
            print('system')
        with open("data.csv", mode="w", encoding='utf-8') as file:
            file_writer = csv.writer(file, delimiter=";", lineterminator="\r")
            file_writer.writerow(message[1:len+1])

start_my_server()