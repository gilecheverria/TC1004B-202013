"""
Read data from the serial port
The data should be generated by Arduino

Gilberto Echeverria
23/10/2020
"""

import serial
import time


def read_loop(port):
    """ Keep reading from the port """
    # An empty list to store the data
    data = []
    while True:
        # How many bytes are currently available to read
        if port.in_waiting > 0:
            # Receive the message from the serial port
            message_bytes = port.readline()
            print(message_bytes)
            # Interpret the bytes as a string
            message = int(message_bytes.decode('utf-8'))
            data.append(message)
            print(data)
        # Do somehting else if there is nothing to read
        else:
            print(".", end='', flush=True)
            time.sleep(0.2)


def main():
    port = serial.Serial(port='/dev/ttyACM0', baudrate=9600)
    read_loop(port)


main()
