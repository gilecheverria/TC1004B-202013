"""
Read data from the serial port
The data should be generated by Arduino

Requires installing pySerial:
    pip install pyserial

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
        # Check the keyboard interrupt to exit this loop
        try:
            # Check there are bytes currently available to read
            if port.in_waiting > 0:
                print()
                # Receive the message from the serial port
                message_bytes = port.readline()
                print(message_bytes)
                # Interpret the bytes as a string
                message = int(message_bytes.decode('utf-8'))
                data.append(message)
                print(data)
            # Do somehting else if there is nothing to read
            else:
                # Just print a dot immediately, and stay on the same line
                print(".", end='', flush=True)
                time.sleep(0.2)
        except KeyboardInterrupt:
            break
    print(f"\nFINAL DATA: {data}")


def main():
    """ Initialize the serial port """
    # CHANGE HERE: the port used by your Arduino
    # If you are using WSL, the port will be:   COM5 -->  /dev/ttyS5
    #                              vvv
    port = serial.Serial(port='/dev/ttyACM0', baudrate=9600)
    read_loop(port)


main()
