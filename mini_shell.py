#!/usr/bin/env python3
import getpass
import socket

import threading
import os

import re

# The theoretical flow of the program is this
#
# This python file process
#           |
#   main mini-shell thread -> Will terminate on "exit" command
#           |
#     -------------------------------
#     |                             |
# foreground program            background program
# (on a seperate thread)         (on a seperate thread)


# This is the main entry point of the shell
def main():
    # define your PATH here
    # PATH values have to be string and they have to be absolute paths
    USER_PATH = ["/home/minhradz/", "/home/minhradz/University/"]

    # temporarily append to the system PATH, this will NOT affect the system PATH after the mini-shell program terminates
    os.environ["PATH"] += os.pathsep + os.pathsep.join(USER_PATH)

    print("Welcome to the mini shell !\n")
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

            # special case when you only do echo
            elif command == "echo":
                print("\n")

            else:
                # create, run and wait for command thread to end
                running_command = command_shell_thread(command)
                running_command.start()

                # we don't join() a background command
                if "&" in command:
                    continue

                running_command.join()


# run all commands as a thread
class command_shell_thread(threading.Thread):
    def __init__(self, command: str):
        super(command_shell_thread, self).__init__()
        # if there is a "->" or "->>", turn the command into ">" or ">>" instead
        # use regex-based substitution
        command = re.sub(r"-(>>)?", r"\1", command)

        if "&" in command:
            # Special case: handles background jobs
            # The only way for this to end is to
            # list all background processes with "jobs" and then
            # either use "kill"
            # or bring it to the foreground with "fg" and the Ctr + C to kill it
            command.replace("&", ""),

        self.command = command

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
    main()
