import json
import os
from pathlib import Path


class MouseMapping:
    MAPPING_ROOT_PATH = Path("mappings/mouse/mappings.json")

    def __init__(self, joystick="LEFT") -> None:
        self.joystick = None
        self.mapping = {
            "RGHT_CLCK": None,
            "LEFT_CLCK": None,
            "SCRL_UP": None,
            "SCRL_DN": None,
        }
        self.set_joystick(joystick)

    def set_joystick(self, joystick):
        self.joystick = joystick
        self.set_mapping()

    def get_joystick(self):
        return self.joystick

    def set_mapping(self):
        if self.joystick == "LEFT":
            self.mapping["SCRL_UP"] = "THROTTLE_INCR"
            self.mapping["SCRL_DN"] = "THROTTLE_DECR"
            self.mapping["RGHT_CLCK"] = "YAW_INCR"
            self.mapping["LEFT_CLCK"] = "YAW_DECR"

        elif self.joystick == "RGHT":
            self.mapping["SCRL_UP"] = "PITCH_INCR"
            self.mapping["SCRL_DN"] = "PITCH_DECR"
            self.mapping["RGHT_CLCK"] = "ROLL_INCR"
            self.mapping["LEFT_CLCK"] = "ROLL_DECR"

    def get_mapping(self):
        return self.mapping
