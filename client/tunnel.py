import threading
from internal_connector import create_local_socket_connection


def handle_incoming_request(request, proxy_socket, local_port):
    internal_socket = None
    try:
        internal_socket = create_local_socket_connection(local_port)
        internal_socket.send(request)
        response = internal_socket.recv(1024)
    except Exception as e:
        response = f"HTTP/1.1 500 Internal Server Error\n\n{str(e)}".encode()
    finally:
        if internal_socket:
            internal_socket.close()
    try:
        proxy_socket.send(response)
    except Exception as e:
        print(f"Error sending response to exposed server. Error: {str(e)}")


def start_client_side_tunnelling(proxy_socket, port):
    while True:
        request = proxy_socket.recv(1024)
        if not request:
            continue
        thread = threading.Thread(target=handle_incoming_request, args=(request, proxy_socket, port))
        thread.start()
