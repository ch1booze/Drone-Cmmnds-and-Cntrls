class Mapping:
    """Maps inputs from Inputter object to its corresponding command."""
    
    def __init__(self, mapping: dict) -> None:
        self.mapping = mapping

    def get_mapping(self):
        return self.mapping

    def get_action(self, key: str):
        return self.mapping.get(key, None)
