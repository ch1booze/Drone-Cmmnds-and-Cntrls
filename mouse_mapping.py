import json
import os
from pathlib import Path


class MouseMapping:
    MAPPING_ROOT_PATH = Path("mappings/mouse/mappings.json")
    CONTROLS = {"t": "Throttle", "y": "Yaw", "p": "Pitch", "r": "Roll"}

    def __init__(self) -> None:
        self.mappings = {}
        self.create_mapping()
        self.get_mapping()

    def get_mapping(self):
        with open(self.MAPPING_ROOT_PATH, "r") as json_obj:
            self.mappings = json.load(json_obj)

    def set_mapping(self):
        mode_name = input("Enter mode name: ")
        print(list(enumerate(self.CONTROLS)))
        control = input("Enter control that is varying: ").lower()

        if control in self.CONTROLS.keys():
            self.mappings[mode_name] = self.CONTROLS[control]

            self.save_mapping()

    def create_mapping(self):
        if not os.path.exists(self.MAPPING_ROOT_PATH):
            self.save_mapping({})

    def save_mapping(self, json_obj=None):
        if not json_obj:
            json_obj = self.mappings

        with open(self.MAPPING_ROOT_PATH, "w") as json_file:
            json.dump(self.mappings, json_file)
