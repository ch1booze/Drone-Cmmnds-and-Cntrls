import os
from pathlib import Path

def folder_exists(folder_path):
    if os.path.exists(folder_path):
        return True

    return False


def create_folder(folder_path):
    os.makedirs(folder_path)


class Scripted:
    SCRIPTING_ROOT_PATH = Path("scripted_files") 
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
    def list_script(self):
        dir_list = os.listdir(self.SCRIPTING_ROOT_PATH)
        script = list(enumerate([f for f in dir_list]))
        return script


    def prewritten_input(self):
        script = [ ]
        actions = list(enumerate([f for f in self.ACTIONS]))
        print(actions)

        while True:
            action = int(input("Enter NUMBER: "))

            # If action is "q", break
            if action == "q":
                break

            line = self.ACTIONS[action]
    
            
            # Collect intensity value i.e. how much should the action change by as a string
            intensity = input("ENTER INTENSITY: ")
            # Concatenate intensity value with line
            line += " " + intensity
            # Add line to script
            script.append(line)
        return script
    def prewritten_write (self):
        script = self.prewritten_input()
        lines = [line + "\n" for line in script]
        print(self.list_script())
        filename =  input("ENTER FILE NAME: ")
        self.write_file(filename, lines)



            
