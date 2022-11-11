import json
import os
from pathlib import Path


def reverse_mapping(dictionary):
    reversed_dict = dict([(v, k) for k, v in dictionary.items()])
    return reversed_dict


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
        "l": "ROLL_INCR"
    }

    def __init__(self) -> None:
        self.check_default_mappings()
        self.mapping = self.get_mapping()

    def list_mappings(self):
        dir_list = os.listdir(self.MAPPING_ROOT_PATH)
        mappings = list(enumerate([f for f in dir_list]))

        return mappings

    def get_mapping(self):
        list_of_mappings = self.list_mappings()

        print(list_of_mappings)
        if len(list_of_mappings) == 1:
            mappings = self.read_mapping(list_of_mappings[0])
        else:
            map_number = int(input("Enter mapping number: "))
            mappings = self.read_mapping(list_of_mappings[map_number])

        return mappings

    def set_mapping(self):
        commands = reverse_mapping(self.mappings)
        print(self.mappings)

        while True:
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

    def write_mapping(self, filename=None):
        list_of_mappings = self.list_mappings()
        print(list_of_mappings)

        if filename:
            map_path = self.MAPPING_ROOT_PATH / (filename + ".json")
        else:
            map_path = self.MAPPING_ROOT_PATH / ("default.json")

        with open(map_path, "r") as json_file:
            json.dump(self.mapping, json_file)

    def check_default_mappings(self):
        if not os.path.isdir(self.MAPPING_ROOT_PATH):
            os.makedirs(self.MAPPING_ROOT_PATH)
            self.write_mapping(self.DEFAULT_MAPPING)
