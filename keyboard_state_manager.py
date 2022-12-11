from utils import string_stripper


class KeyBoardStateManager:
    LEFT_JS = "THROTTLE", "YAW"
    RIGHT_JS = "PITCH", "ROLL"
    EVENT_PRESS = "PRSS"
    EVENT_RELEASE = "RLSE"
    STRIP_LIST = ["_INCR", "_DECR"]

    def __init__(self, mapping) -> None:
        self.mapping = None
        self.set_mapping(mapping)
        self.states = {"THROTTLE": False, "YAW": False, "PITCH": False, "ROLL": False}
        self.js = {"LEFT": None, "RIGHT": None}

    def set_mapping(self, mapping):
        self.mapping = mapping

    def get_mapping(self):
        return self.mapping

    def run(self, event_info):
        event_key, event_type = event_info

        if event_type == self.EVENT_PRESS:
            self.is_pressed(event_key)
        if event_type == self.EVENT_RELEASE:
            self.is_released(event_key)

    def is_pressed(self, key):
        action = self.mapping.get(key, None)
        if action:
            action = string_stripper(action, self.STRIP_LIST)

            if action in self.LEFT_JS:
                self.reset_states("LEFT")
                self.states[action] = True
                self.js["LEFT"] = key

            elif action in self.RIGHT_JS:
                self.reset_states("RIGHT")
                self.states[action] = True
                self.js["RIGHT"] = key

    def is_released(self, key):
        action = self.mapping.get(key, None)
        if action:
            action = string_stripper(action, self.STRIP_LIST)

            if key == self.js["LEFT"]:
                self.reset_states("LEFT")
                self.js["LEFT"] = None
            elif key == self.js["RIGHT"]:
                self.reset_states("RIGHT")
                self.js["RIGHT"] = None

    def reset_states(self, joystick):
        if joystick == "LEFT":
            for a in self.LEFT_JS:
                self.states[a] = False
        elif joystick == "RIGHT":
            for a in self.RIGHT_JS:
                self.states[a] = False

    def get_js(self):
        return tuple(self.js.values())

    def get_states(self):
        return self.states
