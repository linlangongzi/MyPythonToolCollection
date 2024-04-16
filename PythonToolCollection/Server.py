import socket
import threading
import sys

def handle_client_connection(client_socket):
    try:
        print("Client connected. Waiting for data...")
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Received: {data.decode()}")
    except Exception as e:
        print(f"An error occurred in client thread: {e}")
    finally:
        print("Closing connection with the client.")
        client_socket.close()

def start_tcp_server(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        print(f"Starting up on {host} port {port}")
        sock.bind((host, port))
        sock.listen(5)
        while True:
            print("Waiting for a connection...")
            client_socket, address = sock.accept()
            print(f"Connection from {address}")
            client_thread = threading.Thread(target=handle_client_connection, args=(client_socket,))
            client_thread.start()
    except Exception as e:
        print(f"An error occurred in server setup: {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python server.py <IP_Address> <Port>")
    else:
        HOST = sys.argv[1]
        PORT = int(sys.argv[2])
        start_tcp_server(HOST, PORT)
