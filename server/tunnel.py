import json
from internal_connector import create_local_socket_connection

# This will only work when only one request is being tunneled,
# Assume 3 requests are being tunneled, we now have no way to determine which response should be sent to which http_socket_client
# need a way to listen to incoming http requests and send it to the client
# and just wait for response. And a separate thread to listen to the client
# and send the response back to http client socket using the appropriate socket identifying using the Id

def listen_and_forward_http_request_to_client(client_socket, http_port):
    internal_socket = None
    while True:
        internal_socket = create_local_socket_connection(http_port)
        http_client_socket, addr = internal_socket.accept()
        while True:
            request = client_socket.recv(1024)
            if not request:
                http_client_socket.close()
                break
            client_socket.send(request)
            response = http_client_socket.recv(1024)
            http_client_socket.send(response)
        http_client_socket.close()


def start_tunnelling_to_client(client_socket, secret, port):
    request_data = client_socket.recv(1024)
    if not request_data:
        return
    request_argument_string = request_data.decode()
    request_argument = json.loads(request_argument_string)
    # need to validate userId and api key, subdomain's validity and availability using secret json file
    listen_and_forward_http_request_to_client(client_socket, port)
