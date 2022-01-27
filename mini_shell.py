#!/usr/bin/env python3
import getpass
import socket


# the interactive shell will execute all commands and quit on 'exit' command
def main():
    while True:
        command = input(f"{get_username_from_OS()}@{get_hostname_from_OS()}$ ")
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
