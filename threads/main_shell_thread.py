from user_info.user_info import get_hostname_from_OS, get_username_from_OS
from threading import Thread
from threads.command_shell_thread import command_shell_thread


# Interractive shell thread for user input
class caller(Thread):
    def run(self):
        main_thread = main_shell_thread()
        # capture input from
        while True:
            command: str = input(
                f"{get_username_from_OS()}@{get_hostname_from_OS()}$ "
            )

            # Edge case: echo and exit should not be ran with ampersand &
            if "&" in command and ("echo" in command or "exit" in command):
                main_thread.run("echo invalid syntax !")
                continue

            if main_thread.run(command) == -1:
                break


# Shell thread for running pre-determined commands
class main_shell_thread:
    def run(self, command):
        # create, run and wait for command thread to end
        running_command = command_shell_thread(command)
        running_command.start()
        # exit the shell
        if command == "exit":
            return -1
        # we don't join() a background command
        elif "&" in command:
            return 0

        running_command.join()
