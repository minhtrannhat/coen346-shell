from user_info.user_info import get_hostname_from_OS, get_username_from_OS
from threading import Thread
from threads.command_shell_thread import command_shell_thread


# the interactive shell will execute all commands and quit on 'exit' command
class main_shell_thread(Thread):
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

            else:
                # create, run and wait for command thread to end
                running_command = command_shell_thread(command)
                running_command.start()

                # we don't join() a background command
                if "&" in command:
                    continue

                running_command.join()
