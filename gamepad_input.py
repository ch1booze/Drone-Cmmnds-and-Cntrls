""" 
CITATION(S)

Title: Simple joystick test class
Author: Zeth(https://github.com/zeth)
Date: Oct 5, 2018
Availability: https://raw.githubusercontent.com/zeth/inputs/master/examples/jstest.py
"""

import inputs


class GamepadInput:
    """Handles the retrieval of all gamepad events."""

    def __init__(self) -> None:
        self.gamepad = None
        self.set_gamepad()

    def list_gamepads(self):
        """Get name(s) of gamepad(s) connected"""
        gmpds = inputs.devices.gamepads

        return gmpds

    def set_gamepad(self):
        """Select gamepad"""
        gmpds = self.list_gamepads()
        if gmpds:
            self.gamepad = gmpds[0]
        else:
            raise inputs.UnpluggedError("No gamepad found!")

    def get_event(self) -> inputs.InputEvent:
        """Reads gamepad input."""
        try:
            events = self.gamepad.read()
        except EOFError:
            events = []

        return events[0]

    def event_handler(self, event: inputs.InputEvent) -> dict:
        """Resolves event to get relevant information"""
        event_info = {}
        event_info["code"] = event.code
        event_info["event_type"] = event.ev_type
        event_info["state"] - event.state

        return event_info

    def run(self):
        event = self.get_event()
        event_info = self.event_handler(event)

        return event_info


if __name__ == "__main__":
    gp = GamepadInput()

    while True:
        print(gp.run())
        print()
