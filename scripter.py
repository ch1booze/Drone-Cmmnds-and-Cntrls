from pathlib import Path
from utils import list_files, create_folder, printer


class Scripter:
    SCRIPTING_ROOT_PATH = "scriptings"
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
        self.check_default_path()

    def write_file(self, filename, contents):
        with open(self.SCRIPTING_ROOT_PATH + "/" + filename + ".txt", "w") as f:
            f.write(contents)

    def read_file(self, file):
        with open(self.SCRIPTING_ROOT_PATH + "/" + file, "r") as f:
            contents = f.read()

        return contents

    def list_scripts(self):
        return list_files(self.SCRIPTING_ROOT_PATH)

    def check_default_path(self):
        create_folder(self.SCRIPTING_ROOT_PATH)

    def prewritten_script_input(self):
        script = []
        num_of_actions = len(self.ACTIONS)
        actions = {k: self.ACTIONS[k] for k in range(num_of_actions)}
        printer(f"Actions: {actions}")

        while True:
            action = int(input("Enter number(associated with action, 99 to quit): "))
            if action == 99:
                break

            line = self.ACTIONS[action]
            intensity = input("ENTER INTENSITY: ")
            line += " " + intensity

            script.append(line)

        script_str = ""
        for line in script:
            script_str += line + "\n"

        return script_str

    def prewritten_script_writer(self):
        script = self.prewritten_script_input()
        if script:
            printer(f"Scripts: {self.list_scripts()}")
            filename = input("Enter filename: ")

            self.write_file(filename, script)

    def prewritten_script_reader(self):
        contents = None
        scripts = self.list_scripts()
        if scripts:
            printer(scripts)
            script_num = int(input("Enter script number (number not in list to quit): "))
            script = scripts.get(script_num, None)
            if script:
                contents = self.read_file(script)
                contents = contents.splitlines()

        else:
            print("No scripts available")

        return contents
