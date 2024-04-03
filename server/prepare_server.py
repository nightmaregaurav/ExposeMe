import socket
import sys
import settings


def create_proxy_server_socket():
    proxy_socket = None
    try:
        proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        proxy_socket.bind(("127.0.0.1", settings.SERVER_PORT))
        proxy_socket.listen(5)
        return proxy_socket
    except Exception as e:
        print(f"Error establishing connection to exposed server: {str(e)}")
        sys.exit(2)
    finally:
        if proxy_socket:
            proxy_socket.close()
