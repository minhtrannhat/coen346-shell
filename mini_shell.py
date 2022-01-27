#!/usr/bin/env python3
import getpass
import socket
import threading


# the interactive shell will execute all commands and quit on 'exit' command
def main():
    # start the shell thread
    shell = main_shell_thread()
    shell.start()
    shell.join()


class main_shell_thread(threading.Thread):
    def __init__(self):
        super(main_shell_thread, self).__init__()

    def run(self):
        while True:
            command = input(
                f"{get_username_from_OS()}@{get_hostname_from_OS()}$ "
            )
            if command == "exit":
                break
            else:
                execute_command(command)


# get username to display
def get_username_from_OS() -> str:
    return getpass.getuser()


# get hostname to display
def get_hostname_from_OS() -> str:
    return socket.gethostname()


# execute all commands from user
def execute_command(command: str):
    print(command)


if "__main__" == __name__:
    print("Welcome to the mini shell !\n")
    main()
