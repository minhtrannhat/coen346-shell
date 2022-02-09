from threads.main_shell_thread import main_shell_thread
from path.path import set_user_path

set_user_path()

test_thread = main_shell_thread()

commands = [
    "echo hello world",
    "echo hello world -> lol.txt",
    "echo hello world ->> lol.txt",
    "ping 8.8.8.8 -> lol.txt &",
    "a.out",
    "echo &",
    "exit",
]


class Tests:
    def test1(self):
        print("Running test case 1: internal command echo")
        print("Command to run: echo hello world")
        print("Expected output: hello world\n")
        test_thread.run(commands[0])
        print("----------------------------------------------------")

    def test2(self):
        print("Running test case 2: piping with -> ")
        print("Command to run: echo hello world -> lol.txt")
        print("Expected output: lol.txt is created and hello world is in it\n")
        test_thread.run(commands[1])
        print("Running cat lol.txt")
        test_thread.run("cat lol.txt")
        print("----------------------------------------------------")

    def test3(self):
        print("Running test case 3: piping with ->> ")
        print("Command to run: echo hello world ->> lol.txt")
        print(
            "Expected output: lol.txt is appended and there will be another hello world in it\n"
        )
        test_thread.run(commands[2])
        print("Running cat lol.txt")
        test_thread.run("cat lol.txt")
        print("----------------------------------------------------")

    def test4(self):
        print(
            "Running test case 4: external program, background thread and piping"
        )
        print("Command to run: ping 8.8.8.8 -> lol.txt &")
        print("Expected output: lol.txt will keep getting longer\n")
        test_thread.run(commands[3])
        print("----------------------------------------------------")

    def test5(self):
        print("Running test case 5: included executable from a folder in PATH")
        print("Command to run: a.out")
        print("a.out is currently at: ")
        test_thread.run("which a.out")
        print("Expected output: Hello from a internal program!\n")
        test_thread.run(commands[4])
        print("----------------------------------------------------")

    def test6(self):
        print("Running test case 6: invalid syntax")
        print("Command to run: echo &")
        print("Expected output: invalid syntax!\n")
        print("This test case has to be done interactively")
        test_thread.run(commands[5])
        print("----------------------------------------------------")

    def test7(self):
        print("Running test case 7: internal command exit")
        print("Command to run: exit")
        print("Expected output: exits the shell")
        test_thread.run(commands[6])
        print("----------------------------------------------------")


if __name__ == "__main__":
    tests = Tests()
    tests.test1()
    tests.test2()
    tests.test3()
    tests.test4()
    tests.test5()
    tests.test6()
    tests.test7()
