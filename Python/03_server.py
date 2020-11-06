"""
Simple socket example
Server program

Gilberto Echeverria
06/11/2020
"""

import os
import sys
import socket


def init_server(host, port):
    """ Create the server socket """
    # Create a socket to use IPv4 and TCP stream communication
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Associate the socket to the address and port provided
    server_socket.bind( (host, port) )
    # Set the socket to listen for incoming connections
    server_socket.listen(1)
    return server_socket


def wait_for_connections(server_socket):
    """ Keep waiting for an incoming connection """
    while True:
        client_socket, client_address = server_socket.accept()
        pid = os.fork()
        if pid > 0:
            print(f"Received connection from {client_address}")
        elif pid == 0:
            comunication_loop(client_socket)
            sys.exit()
        else:
            print("ERROR: can't fork")


def comunication_loop(client_socket):
    """ Message exchange with the client """
    counter = 0
    again = True
    while again:
        byte_message = client_socket.recv(1024)
        message = byte_message.decode('utf-8')
        counter += 1
        print(f"Got message {counter}: {message}")
        if message == 'Bye':
            reply = 'Bye'.encode('utf-8')
            again = False
        else:
            reply = f"Reply to message {counter}".encode('utf-8')
        client_socket.send(reply)
    client_socket.close()


def main():
    server_socket = init_server('', 8989)
    print("SERVER READY AND LISTENING ON PORT 8989")
    wait_for_connections(server_socket)


main()
