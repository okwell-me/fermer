import socket
from datetime import datetime
import threading

str_to_send = '--no data--'

def start_my_server():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #213.189.201.189
        server.bind(('213.189.201.189', 2000))
        server.listen(4)
        print('Working...')
        while True:
            client_socket, address = server.accept()

            handle_client = threading.Thread(target=client_handler, args=(address, client_socket))
            handle_client.start()

            #data = client_socket.recv(1024).decode('utf-8')
            #process_data(address, data, client_socket)

            #client_socket.shutdown(socket.SHUT_WR)
    except KeyboardInterrupt:
        server.close()
    print('Stop')

def client_handler(address, client_socket):
    data = client_socket.recv(1024).decode('utf-8')
    process_data(address, data, client_socket)
    client_socket.close()

def process_data(address, data, client_socket):
    global str_to_send
    if len(data.split(' ')) > 1:
        if len(data.split(' ')[1]) > 1:
            message: str = data.split(' ')[1]
            message = message.split(';')
            msg_time = datetime.now().strftime('%H:%M:%S')
            msg_len = len(message)
            msg_type = message[0]
            if msg_type == '/DATA':
                msg_from = message[1]

                for i in range(2, msg_len):
                    message[i] = message[i].replace('.', ',')

                str_msg = ' '.join(message[2:msg_len+1])
                str_to_send = str_msg
                print(str(address[0]) + ' [' + msg_time + ']' + ' From ' + msg_from + ' got: ' + str_msg)
                message[1] = msg_time
                with open('/root/fermer/' + msg_from + '_' + datetime.now().strftime('%d-%m-%y') + '.csv', mode='a') as file:
                    file.write(msg_time + ';' + ';'.join(message[2:msg_len+1])+'\n')
            else:
                HDR = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
                client_socket.send(HDR.encode('utf-8') + str_to_send.encode('utf-8'))
        else:
            HDR = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
            client_socket.send(HDR.encode('utf-8') + str_to_send.encode('utf-8'))


if __name__ == '__main__':
    start_my_server()