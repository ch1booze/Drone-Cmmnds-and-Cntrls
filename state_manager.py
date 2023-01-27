from collections import deque

from inputter import EVENT_TYPES
from utils import string_stripper


class StateManager:
    """Manages states of inputs to deteermine which commands need to executed.

    Attributes:
        - mapping: A dict
        - states: A dict
    """

    COMMANDS = "THROTTLE", "YAW", "PITCH", "ROLL"

    def __init__(self, mapping: dict) -> None:
        self.mapping = mapping
        self.states = {
            "THROTTLE": deque([], maxlen=2),
            "YAW": deque([], maxlen=2),
            "PITCH": deque([], maxlen=2),
            "ROLL": deque([], maxlen=2),
        }
        self.reset_states()

    def reset_states(self):
        """Set states of commands to when they are released."""

        self.states = {
            "THROTTLE": deque([], maxlen=2),
            "YAW": deque([], maxlen=2),
            "PITCH": deque([], maxlen=2),
            "ROLL": deque([], maxlen=2),
        }

    def run(self, event_info: dict) -> None:
        """Check if an event type of pressed and released and call the corresponding function.

        Args:
            event_info: A dict that takes the form:
            {
                "key": "<key input from gamepad>",
                "type": <whether or not the event was a press or release>
            }
        """

        if event_info["type"] == EVENT_TYPES[0]:
            self.is_pressed(event_info["key"])

        if event_info["type"] == EVENT_TYPES[1]:
            self.is_released(event_info["key"])

    def is_pressed(self, key) -> None:
        """Adds to queue the most recent command associated with the key pressed.

        Args:
            - key: A character currently being pressed by the keyboard.
        """

        action = self.mapping.get(key, None)
        if action is not None:
            command, command_type = action.split("_")
            if command_type not in self.states[command]:
                self.states[command].appendleft(command_type)

    def is_released(self, key) -> None:
        """Removes from queue the most recent command associated with the key released.

        Args:
            - key: A character currently being released by the keyboard.
        """

        action = self.mapping.get(key, None)
        if action is not None:
            command, command_type = action.split("_")
            if command_type in self.states[command]:
                self.states[command].remove(command_type)

    def get_commands(self) -> list:
        """Returns the list of commands that are to be executed.

        Returns:
            A list of commands that are to be exexuted.
        """

        command_list = []
        for command in self.states:
            if self.states[command]:
                command_str = command + "_" + self.states[command][0]
                command_list.append(command_str)

        return command_list

    def get_reset_states(self) -> dict:
        """Returns the states not currently being executed."""

        reset_states = {
            command: len(self.states[command]) == 0 for command in self.states
        }

        return reset_states


# class StateManager:
#     """
#     Splits mapping to left and right joysticks to allow them to updated simultaneously.

#     Attributes:
#         - mapping: A dict having inputs from Inputter object to its corresponding command.
#         - LEFT_JS, RIGHT_JS:
#         - STRIP_LIST:
#         - states: A dict with commands with their corresponding reset values -
#         True not to reset, False to reset.
#         - js: A dict that stores what input is on the left and the right joysticks.
#     """

#     JOYSTICK = "LEFT", "RIGHT"

#     # Strings that will used to strip commands to their base commands
#     # e.g. THROTTLE_INCR to THROTTLE.
#     STRIP_LIST = "_INCR", "_DECR"

#     # Commands
#     COMMANDS = "THROTTLE", "YAW", "PITCH", "ROLL"

#     def __init__(self, mapping: dict) -> None:
#         self.mapping = mapping
#         self.states = {}
#         self.js = {self.JOYSTICK[0]: None, self.JOYSTICK[1]: None}

#     def get_mapping(self):
#         return self.mapping

#     def run(self, event_info: dict) -> None:
#         """Check if an event type of pressed and released and call the corresponding function.

#         Args:
#             event_info: A dict that takes the form:
#             {
#                 "key": "<key input from gamepad>",
#                 "type": <whether or not the event was a press or release>
#             }
#         """

#         if event_info["type"] == EVENT_TYPES[0]:
#             self.is_pressed(event_info["key"])

#         if event_info["type"] == EVENT_TYPES[1]:
#             self.is_released(event_info["key"])

#     def is_pressed(self, key: str) -> None:
#         """When event type of the key is a press."""

#         # Checks if the key has a corresponding command.
#         # If so, strip command to get base commnd (check STRIP_LIST for more information).

#         action = self.mapping.get(key, None)
#         if action is not None:
#             action = string_stripper(action, self.STRIP_LIST)

#             if action in self.LEFT_JS:
#                 self.reset_states(self.JOYSTICK[0])
#                 self.states[action] = True
#                 self.js[self.JOYSTICK[0]] = key

#             elif action in self.RIGHT_JS:
#                 self.reset_states(self.JOYSTICK[1])
#                 self.states[action] = True
#                 self.js[self.JOYSTICK[1]] = key

#     def is_released(self, key: str) -> None:
#         """When event type of the key is a release."""

#         # Checks if the key has a corresponding command.
#         # If so, strip command to get base commnd (check STRIP_LIST for more information).

#         action = self.mapping.get(key, None)
#         if action is not None:
#             action = string_stripper(action, self.STRIP_LIST)

#             if key == self.js[self.JOYSTICK[0]] or action in self.LEFT_JS:
#                 self.reset_states(self.JOYSTICK[0])
#                 self.js[self.JOYSTICK[0]] = None
#             elif key == self.js[self.JOYSTICK[1]] or action in self.RIGHT_JS:
#                 self.reset_states(self.JOYSTICK[1])
#                 self.js[self.JOYSTICK[1]] = None

#     def reset_states(self, joystick: str) -> None:
#         if joystick == self.JOYSTICK[0]:
#             for s in self.LEFT_JS:
#                 self.states[s] = False
#         elif joystick == self.JOYSTICK[1]:
#             for s in self.RIGHT_JS:
#                 self.states[s] = False

#     def get_states(self) -> dict:
#         return self.states

#     def get_js(self) -> tuple:
#         return tuple(self.js.values())

if __name__ == "__main__":
    from keyboard_mapping import KEYBOARD_MAPPING
    import random

    ksm = StateManager(KEYBOARD_MAPPING)
    letters = ["i", "j", "k", "l", "a", "w", "s", "d"]

    for _ in range(20):
        key = random.choice(letters)
        p_or_r = random.randint(0, 1)

        ksm.run({"key": key, "type": EVENT_TYPES[p_or_r]})
        print(f"Commands: {ksm.get_commands()}")
        print(f"Reset states: {ksm.get_reset_states()}")
        print()
