from utils import printer, list_files


class ScriptExecutor:
    """This handles the execution of scripts that can used to control a DroneControls object.

    Attributes:
        *script: A list containing the current script that contains the commands (of type, str)
        currently being executed.
    """

    SCRIPTING_ROOT_PATH = "scriptings"
    SCRIPT_TYPES = "prewritten", "postwritten"

    def __init__(self) -> None:
        self.script = []

    def read_file(self, file_path: str):
        """This reads a .txt file containing commands to be executed to control a DroneControl object.

        Args:
            *file: The file path from which the commands is to be read from.

        Returns:
            A list of the commands to be executing commands for a DroneControls object.
        """

        with open(self.SCRIPTING_ROOT_PATH + "/" + file_path, "r") as f:
            contents = f.read()

        contents = contents.splitlines()
        return contents

    def get_file_commands(self):
        """Select a .txt file from the folder that stores the scripts.

        Check for the type of the script to be read. Select from a list the names of files of
        the particular type. Load the commands from a file selected.
        """

        # Get the type of script.
        pre_or_post = int(input("Enter 0 for prewritten, 1 for postwritten: "))
        script_path = self.SCRIPT_TYPES[pre_or_post]

        # List the filenames of a particular type.
        file_list = list_files(self.SCRIPTING_ROOT_PATH + "/" + script_path)
        printer({k: file_list[k] for k in range(len(file_list))})

        # Select file from the filenames listed.
        script_number = int(input("Enter number for filename: "))
        script_file = file_list.get(script_number, None)

        # Load commands from file into 'script'.
        if script_number is not None:
            contents = self.read_file(script_path + "/" + script_file)
            self.script = contents

        printer(self.script)
