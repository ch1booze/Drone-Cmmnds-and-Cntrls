import json
import os
from pathlib import Path

from utils import reverse_mapping, list_files


class KeyboardMapping:
    MAPPING_ROOT_PATH = Path("mappings/keyboard")
    DEFAULT_MAPPING = {
        "w": "THROTTLE_INCR",
        "s": "THROTTLE_DECR",
        "a": "YAW_DECR",
        "d": "YAW_INCR",
        "i": "PITCH_INCR",
        "k": "PITCH_DECR",
        "j": "ROLL_DECR",
        "l": "ROLL_INCR",
        "reset": "RESET"
    }

    def __init__(self) -> None:
        self.check_default_mappings()
        self.mapping = self.get_mapping_from_file()

    def list_mappings(self):
        return list_files(self.MAPPING_ROOT_PATH)

    def get_mapping(self):
        return self.mapping

    def get_mapping_from_file(self):
        list_of_mappings = self.list_mappings()

        if len(list_of_mappings) == 1:
            mapping = self.read_mapping(list_of_mappings[0])

        else:
            print(list_of_mappings)

            map_number = int(input("Enter mapping number: "))
            mapping = self.read_mapping(list_of_mappings[map_number])

        return mapping

    def set_mapping(self):
        commands = reverse_mapping(self.mappings)

        while True:
            print(self.mapping)
            old_letter = input(
                "Enter letter for command already mapped to (1 to quit): "
            ).lower()

            if old_letter in commands.values():
                new_letter = input("Enter new letter: ").lower()
                if new_letter.isalpha() and new_letter not in commands.values():
                    commands[self.mappings[new_letter]] = new_letter

            elif old_letter == "1":
                break

        self.mappings = reverse_mapping(commands)

    def read_mapping(self, file):
        map_path = self.MAPPING_ROOT_PATH / file
        with open(map_path, "r") as json_obj:
            mapping = json.load(json_obj)

        return mapping

    def write_mapping(self, filename="default"):
        map_path = self.MAPPING_ROOT_PATH / (filename + ".json")

        with open(map_path, "w") as json_file:
            json.dump(self.mapping, json_file)

    def check_default_mappings(self):
        if not os.path.isdir(self.MAPPING_ROOT_PATH):
            os.makedirs(self.MAPPING_ROOT_PATH)
            self.mapping = self.DEFAULT_MAPPING
            self.write_mapping()

    def get_action(self, key):
        return self.mapping.get(key)
