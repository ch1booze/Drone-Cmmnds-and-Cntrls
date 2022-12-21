import inputs

from inputter import Inputter, EVENT_TYPES


class GamepadInputter(Inputter):
    """Handles gamepad controller inputs as events.

    Attributes:
        event_catcher: A inputs.device.gamepad object that represents the device from which events
        are to be read from.

    Methods:
        *set_event_catcher: This checks through from a list of gamepad controllers that are connected
        to a system. It throws an error when no gamepad controller is found.
        *read_event: Reads and returns an instance of a inputs.InputEvent object.
        *resolve_event: Takes in event data (inputs.InputEvent object) and structures it into information.
        *run_event: Run an instance of "read_event" to get event data and pass it to "resolve_event" to
        obtain and return event information.
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
            events: A inputs.InputEvent object containing the timestamp, code, event type, state, and
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
            event_data: A inputs.InputEvent object containing the timestamp, code, event type, state, and
            of a gamepad input gotten from the 'event_catcher'.

        Returns:
            event_information: A dict that takes the form:
            {
                "key": "<key input from gamepad>",
                "type": <whether or not the event was a press or release>
            }
        """

        # inputs.InputEvent.code being mapped to a event_info["key"] representation
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

        NOT_ABS_STATE_KEYS = ["ABS_Z", "ABS_RZ"]

        # name of gamepad button that has been pressed
        code = event_data.code
        # state can either be pressed(non-zero) or released(zero)
        state = event_data.state
        # this can be Absolute, Key or Synchronised
        ev_type = event_data.ev_type

        event_info = {}
        # when ev_type is not a Synchronised
        if ev_type in ("Absolute", "Key"):
            # when gamepad button is not pressed or pushed i.e. (released)
            if state == 0:
                event_info["type"] = EVENT_TYPES[1]  # the gamepad button is released
                event_info["key"] = code

            # when gamepad button is pressed or pushed
            else:
                event_info["type"] = EVENT_TYPES[0]
                # buttons that have a range of states
                if code not in NOT_ABS_STATE_KEYS and "ABS" in code:
                    if state > 0:
                        key_state = code + "+"
                    elif state < 0:
                        key_state = code + "-"
                    event_info["key"] = KEYS[key_state]
                # buttons that have only two states i.e. zero and one
                else:
                    event_info["key"] = KEYS[code]

        return event_info


if __name__ == "__main__":
    gi = GamepadInputter()
    for _ in range(50):
        print(gi.run_event())
