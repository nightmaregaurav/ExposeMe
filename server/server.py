import os
import sys
from args_parser import parse_arguments, patch_arguments
from prepare_server import create_proxy_server_socket
from client_connector import receive_subscription_from_client

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


def main():
    proxy_socket = None
    try:
        raw_arguments = parse_arguments()
        arguments = patch_arguments(raw_arguments)
        proxy_socket = create_proxy_server_socket()
        receive_subscription_from_client(proxy_socket, arguments["secret"], arguments["port"])
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(2)
    finally:
        if proxy_socket:
            proxy_socket.close()


if __name__ == "__main__":
    main()

