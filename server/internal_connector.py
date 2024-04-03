import socket


def create_local_socket_connection(http_port):
    http_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    http_socket.bind(('127.0.0.1', http_port))
    http_socket.listen(1)
