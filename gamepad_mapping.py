from mapping import Mapping


GAMEPAD_MAPPING = {
    "AnalogL-Up": "THROTTLE_INCR",
    "AnalogL-Down": "THROTTLE_DECR",
    "AnalogL-Left": "YAW_DECR",
    "AnalogL-Right": "YAW_INCR",
    "AnalogR-Up": "PITCH_INCR",
    "AnalogR-Down": "PITCH_DECR",
    "AnalogR-Left": "ROLL_DECR",
    "AnalogR-Right": "ROLL_INCR",
    "ABS_X": "YAW",
    "ABS_Y": "THROTTLE",
    "ABS_RX": "ROLL",
    "ABS_RY": "PITCH",
}


class GamepadMapping(Mapping):
    def __init__(self) -> None:
        super().__init__(GAMEPAD_MAPPING)


if __name__ == "__main__":
    gm = GamepadMapping()
    print(gm.get_mapping())
