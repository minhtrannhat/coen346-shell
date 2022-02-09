from threads.main_shell_thread import main_shell_thread
from path.path import set_user_path

set_user_path()

test_thread = main_shell_thread()


commands = [
    "echo hello",
    "firefox &",
    "a.out &",
    "echo hello world -> lol.txt",
    "echo hello world ->> lol.txt",
    "exit",
]

for command in commands:
    test_thread.run(command)
