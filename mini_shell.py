#!/usr/bin/env python3
import getpass
import socket

import threading
import os
import re


def main():
    # start the shell thread
    shell = main_shell_thread()
    shell.start()
    shell.join()


# the interactive shell will execute all commands and quit on 'exit' command
class main_shell_thread(threading.Thread):
    def __init__(self):
        super(main_shell_thread, self).__init__()

    def run(self):
        while True:
            # capture input from user
            command: str = input(
                f"{get_username_from_OS()}@{get_hostname_from_OS()}$ "
            )

            # exit the shell
            if command == "exit":
                break

            # handles background jobs
            elif "&" in command:
                running_background_command = command_shell_thread(
                    command.split()[0]
                )
                running_background_command.start()
                # we won't have to wait for the thread to finish

            else:
                # if there is a "->" or "->>", turn the command into ">" or ">>" instead
                command = re.sub(r"-(>>)?", r"\1", command)

                # create, run and wait for command thread to end
                running_command = command_shell_thread(command)
                running_command.start()
                running_command.join()


# run all commands as a thread
class command_shell_thread(threading.Thread):
    def __init__(self, command: str):
        super(command_shell_thread, self).__init__()
        self.command: str = command

    def run(self):
        try:
            os.system(self.command)
        except Exception:
            print("mini-shell: command not found: {}".format(self.command))


# get username to display
def get_username_from_OS() -> str:
    return getpass.getuser()


# get hostname to display
def get_hostname_from_OS() -> str:
    return socket.gethostname()


if "__main__" == __name__:
    # define your PATH here
    USER_PATH = ["/home/minhradz/", "/home/minhradz/University/"]

    os.environ["PATH"] += os.pathsep + os.pathsep.join(USER_PATH)

    print(os.environ["PATH"])

    print("Welcome to the mini shell !\n")
    main()
