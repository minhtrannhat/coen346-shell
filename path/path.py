import os


def set_user_path() -> None:
    USER_PATH = [line.strip() for line in open("PATH_NAME.txt", "r")]

    print(USER_PATH)
    # temporarily append to the system PATH, this will NOT affect the system PATH after the mini-shell program terminates
    os.environ["PATH"] += os.pathsep + os.pathsep.join(USER_PATH)
    print(os.environ["PATH"])
