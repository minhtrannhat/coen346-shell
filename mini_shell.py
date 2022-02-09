#!/usr/bin/env python3
from path.path import set_user_path
from threads.main_shell_thread import caller

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
    set_user_path()
    print("Welcome to the mini shell !\n")
    # start the shell thread
    shell = caller()
    shell.start()
    shell.join()


if "__main__" == __name__:
    main()
