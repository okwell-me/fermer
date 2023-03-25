import socket

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
    message_type = data.split(' ')[1]
    print('message type: ')
    if message_type == 'DAT':
        print('data')
    if message_type == 'SYS':
        print('system')

start_my_server()