from abc import ABC, abstractmethod
import time

EVENT_TYPES = "PRSS", "RLSE"  # Press and Release


class Inputter(ABC):
    def __init__(self) -> None:
        self.set_event_catcher()

    @abstractmethod
    def set_event_catcher(self):
        # Sets the input device from event events are to be read from.
        raise NotImplementedError("Input device setter not implemented.")

    @abstractmethod
    def read_event(self):
        # Reads event_data from input device.
        pass

    @abstractmethod
    def resolve_event(self, event_data) -> dict:
        # Resolves event_data into key, state
        pass

    def run_event(self):
        """Read event data via 'read_event' and resolves event data  into information using 'resolve_event'."""

        event_data = self.read_event()
        event_info = self.resolve_event(event_data)

        return event_info
