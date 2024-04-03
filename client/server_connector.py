import socket
import sys
import settings


def get_server_socket_connection():
    proxy_socket = None
    try:
        proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        proxy_socket.connect((settings.SERVER_URL, settings.SERVER_PORT))
        return proxy_socket
    except Exception as e:
        print(f"Error establishing connection to exposed server: {str(e)}")
        sys.exit(2)
    finally:
        if proxy_socket:
            proxy_socket.close()
