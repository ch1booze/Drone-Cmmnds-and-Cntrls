import json
import os
from pathlib import Path


class GamepadMapping:
    # TODO: Create gamepad mapping folder
    # TODO: Create default mapping format
    # TODO: Define set_mapping as seen in keyboard_mapping
    # TODO: Define get_mapping as seen in keyboard_mapping
    # TODO: Define get_mapping_from_file as seen in keyboard_mapping
    # TODO: Define read_mapping from file as seen in keyboard_mapping
    # TODO: Define write_mapping from file as seen in keyboard_mapping
    # TODO: Define get_action from file as seen in keyboard_mapping

    MAPPING_ROOT_PATH = Path("mappings/keyboard")
    DEFAULT_MAPPING = {
        "AnalogL-Up": "THROTTLE_INCR",
        "AnalogL-Down": "THROTTLE_DECR",
        "AnalogL-Left": "YAW_DECR",
        "AnalogR-Right": "YAW_INCR",
        "AnalogR-Up": "PITCH_INCR",
        "AnalogR-Down": "PITCH_DECR",
        "AnalogR-Left": "ROLL_DECR",
        "AnalogR-Right": "ROLL_INCR",
    }

    def __init__(self) -> None:
        pass

    def read_mapping(self, file):
        """Reads a . json file containing mapping information."""
        map_path = self.MAPPING_ROOT_PATH / file

        with open(map_path, "r") as json_obj:
            map_info = json.load(json_obj)

        return map_info

    def write_mapping(self, filename="default"):
        """Writes mapping information to a .json file"""
        map_path = self.MAPPING_ROOT_PATH / filename + ".json"

        with open(map_path, "w") as json_file:
            json.dump(self.mapping, json_file)

    
