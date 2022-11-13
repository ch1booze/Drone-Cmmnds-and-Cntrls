from pathlib import Path
from utils import list_files, create_folder


class Scripter:
    SCRIPTING_ROOT_PATH = Path("scriptings")
    ACTIONS = [
        "THROTTLE_INCR",
        "THROTTLE_DECR",
        "YAW_DECR",
        "YAW_INCR",
        "PITCH_INCR",
        "PITCH_DECR",
        "ROLL_DECR",
        "ROLL_INCR",
    ]

    def __init__(self) -> None:
        pass

    def write_file(self, filename, contents):
        with open(filename + ".txt", "w") as f:
            f.write(contents)

    def read_file(self, filename):
        with open(filename + ".txt", "r") as f:
            contents = f.read("file")

        return contents

    def list_scripts(self):
        return list_files(self.SCRIPTING_ROOT_PATH)

    def check_default_path(self):
        create_folder(self.SCRIPTING_ROOT_PATH)

    def prewritten_script_input(self):
        script = []
        actions = list(enumerate([f for f in self.ACTIONS]))
        print(actions)

        while True:
            action = int(input("Enter number(associated with action): "))
            if action == "q":
                break

            line = self.ACTIONS[action]
            intensity = input("ENTER INTENSITY: ")
            line += " " + intensity

            script.append(line)
        script = [line + "\n" for line in script]

        return script

    def prewritten_script_writer(self):
        script = self.prewritten_script_input()
        print(self.list_script())
        filename = input("Enter filename: ")

        self.write_file(filename, script)
