import json
import os
import sys
from args_parser import parse_arguments, patch_arguments
from server_connector import get_server_socket_connection
from tunnel import start_client_side_tunnelling

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


def main():
    proxy_socket = None
    try:
        raw_arguments = parse_arguments()
        arguments = patch_arguments(raw_arguments)
        proxy_socket = get_server_socket_connection()
        arguments_as_string = json.dumps(arguments)
        proxy_socket.send(arguments_as_string.encode())
        start_client_side_tunnelling(proxy_socket, arguments["port"])
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(2)
    finally:
        if proxy_socket:
            proxy_socket.close()


if __name__ == "__main__":
    main()
