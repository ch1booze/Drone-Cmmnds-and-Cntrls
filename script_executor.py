import time
from drone_controls import DroneControls


class ScriptExecutor:
    def __init__(self, commands) -> None:
        self.commands = commands
        self.cntrls = DroneControls()

    def run(self):
        for command in self.commands:
            action, intensity = command.split(" ")
            for _ in range(int(intensity)):
                self.cntrls.get_outcome(action)
                time.sleep(0.3)

            print(f"Values: {self.cntrls.get_values()})")
            self.cntrls.reset()
