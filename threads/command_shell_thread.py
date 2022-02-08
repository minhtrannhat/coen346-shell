from threading import Thread
from re import sub
from os import system


# run all commands as a thread
class command_shell_thread(Thread):
    def __init__(self, command: str):
        super(command_shell_thread, self).__init__()
        # if there is a "->" or "->>", turn the command into ">" or ">>" instead
        # use regex-based substitution
        command = sub(r"-(>>)?", r"\1", command)

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
            system(self.command)
        except Exception:
            print("mini-shell: command not found: {}".format(self.command))
