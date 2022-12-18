from mapping import Mapping

KEYBOARD_MAPPING = {
        "w": "THROTTLE_INCR",
        "s": "THROTTLE_DECR",
        "a": "YAW_DECR",
        "d": "YAW_INCR",
        "i": "PITCH_INCR",
        "k": "PITCH_DECR",
        "j": "ROLL_DECR",
        "l": "ROLL_INCR",
    }

class KeyboardMapping(Mapping):
    def __init__(self) -> None:
        super().__init__(KEYBOARD_MAPPING)