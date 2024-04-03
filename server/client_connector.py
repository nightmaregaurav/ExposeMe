import threading

from tunnel import start_tunnelling_to_client


def receive_subscription_from_client(server_socket, secret, port):
    while True:
        client_socket, addr = server_socket.accept()
        client_thread = threading.Thread(target=start_tunnelling_to_client, args=(client_socket, secret, port))
        client_thread.start()
