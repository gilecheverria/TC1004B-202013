"""
Simple socket example
Client program

Gilberto Echeverria
06/11/2020
"""

import socket


def connect_to_server(host, port):
    """ Create the client socket """
    # Create a socket to use IPv4 and TCP stream communication
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to the server
    client_socket.connect( (host, port) )
    return client_socket


def comunication_loop(client_socket):
    """ Message exchange with the server """
    again = True
    while again:
        # Send a message
        message = input("Enter message: ")
        if message == 'Bye':
            again = False
        byte_message = message.encode('utf-8')
        client_socket.send(byte_message)
        # Wait for the reply
        byte_reply = client_socket.recv(1024)
        reply = byte_reply.decode('utf-8')
        print(f"Got reply {reply}")
    client_socket.close()

def main():
    client_socket = connect_to_server('127.0.0.1', 8989)
    comunication_loop(client_socket)


main()
