import inputs

from inputter import Inputter, EVENT_TYPES


class GamepadInputter(Inputter):
    """Handles gamepad controller inputs as events.

    Attributes:
        *event_catcher: A inputs.device.gamepad object that represents the device from which events
        are to be read from.
    """

    def set_event_catcher(self):
        """Selects gamepad from which event events are to be read from.

        Raise:
            *inputs.UnpluggedError: This happens when no gamepad is connected to the system."""

        gmpds = inputs.devices.gamepads
        if gmpds:
            self.event_catcher = gmpds[0]
        else:
            raise inputs.UnpluggedError("No gamepad found!")

    def read_event(self):
        """Reads an event from the gamepad set by the 'event_catcher'.

        Returns:
            A inputs.InputEvent object containing the timestamp, code, event type, state, and
            of a gamepad input gotten from the 'event_catcher'.
        """

        try:
            events = self.event_catcher.read()
        except EOFError:
            events = []
        return events[0]

    def resolve_event(self, event_data: inputs.InputEvent) -> dict:
        """Returns a structured event information from gamepad event data.

        Args:
            *event_data: A inputs.InputEvent object containing the timestamp, code, event type, state, and
            of a gamepad input gotten from the 'event_catcher'.

        Returns:
            A dict that takes the form:
            {
                "key": "<key input from gamepad>",
                "type": <whether or not the event was a press or release>
            }
        """

        # An inputs.InputEvent.code being mapped to a user-friendly representation
        KEYS = {
            "BTN_TL": "L1",
            "ABS_Z": "L2",
            "BTN_TR": "R1",
            "ABS_RZ": "R2",
            "BTN_SELECT": "Select",
            "BTN_START": "Start",
            "BTN_NORTH": "North",
            "BTN_EAST": "East",
            "BTN_SOUTH": "South",
            "BTN_WEST": "West",
            "ABS_HAT0Y-": "D-Up",
            "ABS_HAT0X-": "D-Left",
            "ABS_HAT0X+": "D-Right",
            "ABS_HAT0Y+": "D-Down",
            "ABS_Y+": "AnalogL-Up",
            "ABS_X-": "AnalogL-Left",
            "ABS_X+": "AnalogL-Right",
            "ABS_Y-": "AnalogL-Down",
            "ABS_RY+": "AnalogR-Up",
            "ABS_RX-": "AnalogR-Left",
            "ABS_RX+": "AnalogR-Right",
            "ABS_RY-": "AnalogR-Down",
        }

        NOT_ABS_STATE_KEYS = "ABS_Z", "ABS_RZ"

        # Name of gamepad button that has been pressed
        code = event_data.code
        # Can either be pressed(non-zero) or released(zero).
        state = event_data.state
        # This can be Absolute, Key or Synchronised.
        ev_type = event_data.ev_type

        event_info = {}
        if ev_type in ("Absolute", "Key"):
            # When gamepad button is not pressed or pushed i.e. (released).
            if state == 0:
                event_info["type"] = EVENT_TYPES[1]  # When gamepad button is released
                event_info["key"] = code

            # When gamepad button is pressed or pushed
            else:
                event_info["type"] = EVENT_TYPES[0]
                # Gamepad buttons that have a range of states
                if code not in NOT_ABS_STATE_KEYS and "ABS" in code:
                    if state > 0:
                        key_state = code + "+"
                    elif state < 0:
                        key_state = code + "-"
                    event_info["key"] = KEYS[key_state]
                # Gamepad buttons that have only two states i.e. zero and one
                else:
                    event_info["key"] = KEYS[code]

        return event_info


if __name__ == "__main__":
    gi = GamepadInputter()
    for _ in range(50):
        print(gi.run_event())
