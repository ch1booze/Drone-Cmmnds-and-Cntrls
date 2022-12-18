from abc import ABC


class Mapping(ABC):
    def __init__(self, mapping) -> None:
        self.set_mapping(mapping)

    def set_mapping(self, mapping):
        self.mapping = mapping

    def get_mapping(self):
        return self.mapping

    def get_action(self, key: str):
        return self.mapping.get(key, None)
