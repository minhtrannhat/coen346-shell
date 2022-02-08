#!/usr/bin/env python3
import getpass
import socket
import threading
import os


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
<<<<<<< Updated upstream
            else:
                execute_command(command)
=======

            # special case when you only do echo
            elif command == "echo":
                print(command.split("echo ")[1])
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
        
        if "->>" in command:
            File_Name=command.split("->> ")[1]
            command = (command.split("->>")[0])
            self.command = command
            temp= str(os.system(self.command))
            with open(File_Name, "a") as f:
                f.write(temp)
                f.close()
        elif "->" in command:
            File_Name=command.split("-> ")[1]
            command = (command.split("->")[0])
            self.command = command
            temp= str(os.system(self.command))
            with open(File_Name, "w") as f:
                f.write(temp)
        if "&" in command:
            # Special case: handles background jobs
            # The only way for this to end is to
            # list all background processes with "jobs" and then
            # either use "kill"
            # or bring it to the foreground with "fg" and the Ctr + C to kill it
            command.replace("&", "")

        self.command = command

    def run(self):
        try:
            os.system(self.command)
        except Exception:
            print("mini-shell: command not found: {}".format(self.command))
>>>>>>> Stashed changes


# get username to display
def get_username_from_OS() -> str:
    return getpass.getuser()


# get hostname to display
def get_hostname_from_OS() -> str:
    return socket.gethostname()


# execute all commands from user
def execute_command(command: str):
    os.system(command)


if "__main__" == __name__:
    print("Welcome to the mini shell !\n")
    main()
