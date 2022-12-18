from abc import ABC

from inputter import EVENT_TYPES
from utils import string_stripper


class StateManager(ABC):
    JOYSTICK = "LEFT", "RIGHT"

    def __init__(self, mapping) -> None:
        self._left_js = "THROTTLE", "YAW"
        self._right_js = "PITCH", "ROLL"
        self._strip_list = "_INCR", "_DECR"
        self._states = {"THROTTLE": False, "YAW": False, "PITCH": False, "ROLL": False}
        self._js = {self.JOYSTICK[0]: None, self.JOYSTICK[1]: None}

        self.set_mapping(mapping)

    def set_mapping(self, mapping: dict) -> None:
        self.mapping = mapping

    def get_mapping(self):
        return self.mapping

    def run(self, event_info: dict) -> None:
        print(event_info)
        if event_info["type"] == EVENT_TYPES[0]:
            self._is_pressed(event_info["key"])

        if event_info["type"] == EVENT_TYPES[1]:
            self._is_released(event_info["key"])

    def _is_pressed(self, key: str) -> None:
        action = self.mapping.get(key, None)
        if action:
            action = string_stripper(action, self._strip_list)

            if action in self._left_js:
                self._reset_states(self.JOYSTICK[0])
                self._states[action] = True
                self._js[self.JOYSTICK[0]] = key

            elif action in self._right_js:
                self._reset_states(self.JOYSTICK[1])
                self._states[action] = True
                self._js[self.JOYSTICK[1]] = key

    def _is_released(self, key: str) -> None:
        action = self.mapping.get(key, None)
        if action:
            action = string_stripper(action, self._strip_list)

            if key == self._js[self.JOYSTICK[0]] or action in self._left_js:
                self._reset_states(self.JOYSTICK[0])
                self._js[self.JOYSTICK[0]] = None
            elif key == self._js[self.JOYSTICK[1]] or action in self._right_js:
                self._reset_states(self.JOYSTICK[1])
                self._js[self.JOYSTICK[1]] = None

    def _reset_states(self, joystick):
        if joystick == self.JOYSTICK[0]:
            for s in self._left_js:
                self._states[s] = False
        elif joystick == self.JOYSTICK[1]:
            for s in self._right_js:
                self._states[s] = False

    def get_states(self):
        return self._states

    def get_js(self):
        return tuple(self._js.values())
