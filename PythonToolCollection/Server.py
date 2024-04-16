
import socket
import sys

import socket
import threading

def handle_client_connection(client_socket):
    """
    Handles a client connection, receives data from the client, and optionally sends a response.
    """
    try:
        print("Client connected. Waiting for data...")
        while True:
            # Receive data from the client
            data = client_socket.recv(1024)
            if not data:
                # No more data from client, connection can be closed
                break
            print(f"Received: {data.decode()}")
            
            # Optional: Echo the received data back to the client
            # client_socket.sendall(data)
        print("No more data. Closing connection with the client.")
        
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client_socket.close()

def start_tcp_server(host, port):
    """
    Starts a TCP server that listens on a specified host and port, accepts incoming connections,
    and creates a new thread to handle each connection.
    """
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the server address and port
    server_address = (host, port)
    print(f"Starting up on {host} port {port}")
    sock.bind(server_address)
    
    # Listen for incoming connections
    sock.listen(5)
    
    while True:
        # Wait for a connection
        print("Waiting for a connection...")
        client_socket, address = sock.accept()
        print(f"Connection from {address}")
        
        # Handle client connection in a new thread
        client_thread = threading.Thread(target=handle_client_connection, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    HOST, PORT = "127.0.0.1", 5002  # Listen on all network interfaces
    start_tcp_server(HOST, PORT)
