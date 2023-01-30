from utils import create_folder, list_files, printer, string_stripper, write_file


class PrewrittenScripter:
    """ """

    SCRIPTING_ROOT_PATH = "scriptings/prewritten"
    ACTIONS = {
        0: "THROTTLE_INCR",
        1: "THROTTLE_DECR",
        2: "YAW_DECR",
        3: "YAW_INCR",
        4: "PITCH_INCR",
        5: "PITCH_DECR",
        6: "ROLL_DECR",
        7: "ROLL_INCR",
    }

    def __init__(self) -> None:
        self.check_default_path()
        self.script = []

    def list_scripts(self):
        """List filenames that are in prewritten scripts folder."""

        return list_files(self.SCRIPTING_ROOT_PATH)

    def check_default_path(self):
        """Checks if path to which scripts (.txt) files are to be saved exists."""

        create_folder(self.SCRIPTING_ROOT_PATH)

    def prewritten_script_input(self):
        """Records user input for commands to be prewritten.

        Command types will be entered using numbers using
            ACTIONS = {
                0: "THROTTLE_INCR", 1: "THROTTLE_DECR",
                2: "YAW_DECR", 3: "YAW_INCR",
                4: "PITCH_INCR", 5: "PITCH_DECR",
                6: "ROLL_DECR", 7: "ROLL_INCR"
            }
        Commands associated with joysticks:
            LEFT_JS = "THROTTLE", "YAW"
            RIGHT_JS = "PITCH", "ROLL"

        NB: To enter command types with left and right joysticks,
        enter number in left and right joystick commands to run.
        """

        printer(f"Actions: {self.ACTIONS}")

        while True:
            actions = input(
                "Enter number(s) (associated with action(s), 'q' to quit): "
            )
            if actions == "q":
                break

            intensity = input("Enter intensity: ")
            script_line = self.script_formatter(actions, intensity)
            if script_line:
                self.script.append(script_line)

    def action_validator(self, action_list):
        strip_list = "_INCR", "_DECR"
        action_stripped_list = set(
            [string_stripper(a, strip_list) for a in action_list]
        )

        return len(action_list) == len(action_stripped_list)

    def script_formatter(self, actns, intnsty):
        line = ""
        actions = actns.replace(" ", "")
        intensity = int(intnsty)

        action_list = [self.ACTIONS[int(a)] for a in actions]
        if self.action_validator(action_list):
            for action in action_list:
                line += action + " "

            line += f"{intensity}\n"

        return line

    def prewritten_script_writer(self):
        print("----------------------------")
        self.prewritten_script_input()

        if self.script:
            printer(f"Scripts: {self.list_scripts()}")
            filename = input("Enter filename: ")

            write_file(
                folder_path=self.SCRIPTING_ROOT_PATH,
                file_contents=self.script,
                filename=filename,
            )
        print("----------------------------")


if __name__ == "__main__":
    prewrttn_scrptr = PrewrittenScripter()
    prewrttn_scrptr.prewritten_script_writer()
