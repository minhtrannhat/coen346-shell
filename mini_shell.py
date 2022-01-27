#!/usr/bin/env python3
import getpass
import socket


def main():
    while True:
        command = input(f"{get_username_from_OS()}@{get_hostname_from_OS()}$ ")
        if command == "exit":
            break
        else:
            print(command)


def get_username_from_OS() -> str:
    return getpass.getuser()


def get_hostname_from_OS() -> str:
    return socket.gethostname()


if "__main__" == __name__:
    main()
