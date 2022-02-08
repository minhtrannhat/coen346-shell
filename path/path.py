import os


def set_user_path() -> None:
    # define your PATH here
    # PATH values have to be string and they have to be absolute paths
    with open("PATH_NAME.txt") as f:
        USER_PATH=f.readlines()
    print(USER_PATH)
    # temporarily append to the system PATH, this will NOT affect the system PATH after the mini-shell program terminates
    os.environ["PATH"] += os.pathsep + os.pathsep.join(USER_PATH)
