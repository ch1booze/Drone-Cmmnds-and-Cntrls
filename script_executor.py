import time

from drone_controls import DroneControls
from utils import printer


class ScriptExecutor:
    SCRIPTING_ROOT_PATH = "scriptings"

    def __init__(self, controls: DroneControls) -> None:
        self.script = None
        self.cntrls = controls

    def read_file(self, file):
        with open(self.SCRIPTING_ROOT_PATH + "/" + file, "r") as f:
            contents = f.read()

        return contents

    def script_reader(self):
        scripts = self.list_scripts()
        if scripts:
            printer(scripts)
            script_num = int(
                input("Enter script number (number not in list to quit): ")
            )
            script_path = scripts.get(script_num, None)
            if script_path:
                self.script = self.read_file(script_path)
                self.script = self.script.splitlines()
        else:
            print("No scripts available")

    def run(self):
        self.script_reader()
        if self.script:
            for command in self.script:
                script_line = command.split(" ")
                actions, intensity = script_line[:-1], script_line[-1]

                for _ in range(int(intensity)):
                    for a in actions:
                        self.cntrls.get_outcome(a)
                    time.sleep(0.01)

                    print(f"Values: {self.cntrls.get_values()})")
                    self.cntrls.reset()
                    print(f"Values: {self.cntrls.get_values()})")
