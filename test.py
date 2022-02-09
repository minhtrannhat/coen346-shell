import mini_shell
from threads.main_shell_thread import main_shell_thread

command = "echo hello"

main_shell_thread.run(command)
