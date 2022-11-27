class MouseStateManager:
    EVENT_CLICK = "CLCK"
    EVENT_SCROLL = "SCRL"

    def __init__(self, mapping) -> None:
        self.mapping = None
        self.set_mapping(mapping)
        self.states = {"LEFT_JS": None, "RIGHT_JS": None}

    def set_mapping(self, mapping):
        self.mapping = mapping

    def get_mapping(self):
        return self.mapping

    def run(self, event_info):
        if event_info[0] == self.EVENT_CLICK:
            self.states["LEFT_JS"] = ...
        elif event_info[0] == self.EVENT_SCROLL:
            self.states["LEFT_JS"] = ...
            