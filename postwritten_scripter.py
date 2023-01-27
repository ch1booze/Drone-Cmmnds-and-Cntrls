from datetime import datetime

from utils import create_folder, list_files, printer, write_file


class PostwrittenScripter:
    """"""

    SCRIPTING_ROOT_PATH = "scriptings/postwritten"

    def __init__(self) -> None:
        self.check_default_path()
        self.script = []
        self.command_list = []
        self.mag = 0

    def check_default_path(self):
        """Checks if path to which scripts (.txt) files are to be saved exists."""

        create_folder(self.SCRIPTING_ROOT_PATH)

    def list_scripts(self):
        """List filenames that are in postwritten scripts folder."""

        return list_files(self.SCRIPTING_ROOT_PATH)

    def check_commands(self, command_list: list):
        if self.command_list != command_list:
            if len(self.command_list) > 0:
                self.add_script_line()

            self.command_list = command_list
            self.mag = 1

        else:
            self.mag += 1

    def add_script_line(self):
        line = ""
        for command in self.command_list:
            line += command + " "
        line += f"{self.mag}"
        print(f"-> {line}")

        line += "\n"
        self.script.append(line)

    def postwritten_script_writer(self) -> None:
        """Saves script currently recorded into a .txt file."""

        if self.script:
            now = datetime.now()
            filename = (
                f"{now.year}{now.month}{now.day}_{now.hour}{now.minute}{now.second}"
            )

            write_file(
                folder_path=self.SCRIPTING_ROOT_PATH,
                file_contents=self.script,
                filename=filename,
            )
            self.script = []  # Reset 'script'

            print("----------------------------")
            print()
            print(f"Script saved at {filename}.txt")
            print()
            print("----------------------------")


if __name__ == "__main__":
    from keyboard_mapping import KEYBOARD_MAPPING
    import random
    from state_manager import StateManager, EVENT_TYPES

    ksm = StateManager(KEYBOARD_MAPPING)
    letters = ["i", "j", "k", "l", "a", "w", "s", "d"]
    p = PostwrittenScripter()

    for _ in range(20):
        key = random.choice(letters)
        p_or_r = random.randint(0, 1)

        print(f"Key: {key}")

        ksm.run({"key": key, "type": EVENT_TYPES[p_or_r]})
        cl = ksm.get_commands()
        print(f"Commands: {cl}")
        print(f"Reset states: {ksm.get_reset_states()}")

        p.check_commands(cl)

        print(f"Script: {p.script}")
        print()
