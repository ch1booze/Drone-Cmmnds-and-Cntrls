import time
from drone_controls import DroneControls


class ScriptExecutor:
    def __init__(self, commands) -> None:
        self.commands = commands
        self.cntrls = DroneControls()

    def run(self):
        for command in self.commands:
            script_line = command.split(" ")
            actions, intensity = script_line[:-1], script_line[-1]

            for _ in range(int(intensity)):
                for a in actions:
                    self.cntrls.get_outcome(a)
                time.sleep(0.01)

                print(f"Values: {self.cntrls.get_values()})")
                self.cntrls.reset()
                print(f"Values: {self.cntrls.get_values()})")
