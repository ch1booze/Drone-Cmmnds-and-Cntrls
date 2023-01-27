from utils import create_folder, list_files, printer, string_stripper, write_file


class PrewrittenScripter

# class PrewrittenScripter:
#     """This writes commands that will be executed by a DroneControls object.

#     'Pre' in PrewrittenScripter means written before the commands are executed.
#     Format of commands script is:
#         # example.txt
#         THROTTLE_DECR 24
#         YAW_INCR PITCH_INCR 30
#         ROLL_INCR 23

#     NB: A command can has one or two command types. When two, it means both left and right joysticks have been pressed
#     simultaneously. The number at the end is the number of times it should run for.

#     Attributes:
#         *script: A list of the commands that are being executed by a DroneControl object.
#     """

#     SCRIPTING_ROOT_PATH = "scriptings/prewritten"
#     LEFT_JS = "THROTTLE", "YAW"
#     RIGHT_JS = "PITCH", "ROLL"
#     ACTIONS = {
#         0: "THROTTLE_INCR",
#         1: "THROTTLE_DECR",
#         2: "YAW_DECR",
#         3: "YAW_INCR",
#         4: "PITCH_INCR",
#         5: "PITCH_DECR",
#         6: "ROLL_DECR",
#         7: "ROLL_INCR",
#     }
#     STRIP_LIST = "_INCR", "_DECR"

#     def __init__(self) -> None:
#         self.check_default_path()
#         self.script = []

#     def list_scripts(self):
#         """List filenames that are in prewritten scripts folder."""

#         return list_files(self.SCRIPTING_ROOT_PATH)

#     def check_default_path(self):
#         """Checks if path to which scripts (.txt) files are to be saved exists."""

#         create_folder(self.SCRIPTING_ROOT_PATH)

#     def script_formatter(self, actions: str, intensity: str) -> str:
#         """Parses the command types('actions') and magnitude('intensity') to a string to be added to the script.

#         Args:
#             *actions: A number or numbers in form of a str for commands type(s).
#             *intensity: A number in form of a str for the magnitude associated the 'actions'.

#         Returns:
#             A str in the format of:
#                 THROTTLE_DECR 24
#                 YAW_INCR PITCH_INCR 30
#             to added to the list of commands being recorded.
#         """

#         # Change to integers
#         action_nums = tuple(int(i) for i in actions.split())
#         intensity_num = int(intensity)

#         # Get the actions associated
#         action_list = [self.ACTIONS[a] for a in action_nums]
#         len_action_list = len(action_list)

#         script_line = []

#         if len_action_list == 1:  # Single command
#             script_line.append(action_list[0])
#         elif len_action_list == 2:  # Simultaneous commands
#             validity = self.action_validator(action_list)
#             if validity:
#                 for i in range(len_action_list):
#                     script_line.append(action_list[i])

#         script_line.append(intensity_num)

#         if len_action_list > 2:
#             raise Exception("Invalid number of inputs.")

#         script_line = [str(s) for s in script_line]
#         script_line = " ".join(script_line)
#         script_line += "\n"

#         return script_line

#     def action_validator(self, action_list: tuple) -> bool:
#         """Validates actions entered (when actions entered are two) belong to separate joysticks

#         Args:
#             *action_list: A tuple conataining actions being checked for validity.
#         """

#         action_list_stripped = (
#             string_stripper(a, self.STRIP_LIST) for a in action_list
#         )
#         action_js = ["l" if a in self.LEFT_JS else "r" for a in action_list_stripped]

#         return action_js[0] != action_js[1]

#     def prewritten_script_input(self):
#         """Records user input for commands to be prewritten.

#         Command types will be entered using numbers using
#             ACTIONS = {
#                 0: "THROTTLE_INCR", 1: "THROTTLE_DECR",
#                 2: "YAW_DECR", 3: "YAW_INCR",
#                 4: "PITCH_INCR", 5: "PITCH_DECR",
#                 6: "ROLL_DECR", 7: "ROLL_INCR"
#             }
#         Commands associated with joysticks:
#             LEFT_JS = "THROTTLE", "YAW"
#             RIGHT_JS = "PITCH", "ROLL"

#         NB: To enter command types with left and right joysticks,
#         enter number in left and right joystick commands to run.
#         """

#         printer(f"Actions: {self.ACTIONS}")

#         while True:
#             actions = input(
#                 "Enter number(s) (associated with action(s), 'q' to quit): "
#             )
#             if actions == "q":
#                 break

#             intensity = input("Enter intensity: ")
#             script_line = self.script_formatter(actions, intensity)
#             if script_line:
#                 self.script.append(script_line)

#     def prewritten_script_writer(self):
#         """Saves script currently recorded into a .txt file."""

#         self.script = []

#         print("----------------------------")
#         self.prewritten_script_input()

#         if self.script:
#             printer(f"Scripts: {self.list_scripts()}")
#             filename = input("Enter filename: ")

#             write_file(
#                 folder_path=self.SCRIPTING_ROOT_PATH,
#                 file_contents=self.script,
#                 filename=filename,
#             )
#         print("----------------------------")
        


if __name__ == "__main__":
    prewrttn_scrptr = PrewrittenScripter()
    prewrttn_scrptr.prewritten_script_writer()
