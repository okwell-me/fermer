import socket

def start_my_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('213.189.201.189', 2000))
    server.listen(4)
    print('Working...')
    while True:
        client_socket, address = server.accept()
        data = client_socket.recv(1024).decode('utf-8')
        #content = 'Im alive ok'.encode('utf-8')
        content = load_page_get(data)
        client_socket.send(content)
        client_socket.shutdown(socket.SHUT_WR)
    print('Stop')

def load_page_get(request_data):
    HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
    HDRS_404 = 'HTTP/1.1 404 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
    path = request_data.split(' ')[1]
    response = ''
    try:
        with open('views'+path, 'rb') as file:
            response = file.read()
        return HDRS.encode('utf-8') + response
    except FileNotFoundError:
        return (HDRS_404 + 'Bruh.........').encode('utf-8')

start_my_server()