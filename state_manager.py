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
