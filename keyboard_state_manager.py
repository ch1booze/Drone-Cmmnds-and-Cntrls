from utils import string_stripper


class KeyBoardStateManager:
    LEFT_JS = ["THROTTLE", "YAW"]
    RIGHT_JS = ["PITCH", "ROLL"]
    EVENT_PRESS = "PRSS"
    EVENT_RELEASE = "RLSE"
    STRIP_LIST = ["_INCR", "_DECR"]

    def __init__(self, mapping) -> None:
        self.mapping = None
        self.set_mapping(mapping)
        self.states = {"LEFT_JS": None, "RIGHT_JS": None}

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
                self.states["LEFT_JS"] = key
            elif action in self.RIGHT_JS:
                self.states["RIGHT_JS"] = key

    def is_released(self, key):
        action = self.mapping.get(key, None)
        if action:
            action = self.mapping[key]
            action = string_stripper(action, self.STRIP_LIST)

            if action in self.LEFT_JS:
                if key == self.states["LEFT_JS"]:
                    self.states["LEFT_JS"] = None
            elif action in self.RIGHT_JS:
                if key == self.states["RIGHT_JS"]:
                    self.states["RIGHT_JS"] = None

    def get_states(self):
        return tuple(self.states.values())
