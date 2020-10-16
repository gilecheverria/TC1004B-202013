"""
Simple example of using fork to create new processes

Gil Echeverria
16/10/2020
"""

import os
import time


def parent_action(child_pid):
    print(f"This is the parent. PID: {os.getpid()}")
    print(f"My child is {child_pid}")


def child_action():
    time.sleep(2)
    print(f"  Child process. PID: {os.getpid()}")
    print(f"  My parent is {os.getppid()}")


def main():
    print("Program start")
    # Create a copy of this process, using 'fork'
    pid = os.fork()
    # The value returned will be different in each process
    if pid > 0:
        # Parent process
        parent_action(pid)
    elif pid == 0:
        # Child process
        child_action()
    else:
        print("Error when creating process")
    print(f"Process {os.getpid()} finishing")


main()
