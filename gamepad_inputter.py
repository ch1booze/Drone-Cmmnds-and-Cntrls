import inputs

from inputter import Inputter, EVENT_TYPES


class GamepadInputter(Inputter):
    def _set_event_catcher(self):
        """Select gamepad"""
        gmpds = inputs.devices.gamepads
        if gmpds:
            self._event_catcher = gmpds[0]
        else:
            raise inputs.UnpluggedError("No gamepad found!")

    def read_event(self):
        try:
            events = self._event_catcher.read()
        except EOFError:
            events = []

        return events[0]

    def resolve_event(self, event_data: inputs.InputEvent) -> dict:
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

        code = event_data.code
        state = event_data.state
        ev_type = event_data.ev_type

        event_info = {}
        if ev_type in ("Absolute", "Key"):
            if state == 0:
                event_info["type"] = EVENT_TYPES[1]
                event_info["key"] = code

            else:
                event_info["type"] = EVENT_TYPES[0]
                if code not in NOT_ABS_STATE_KEYS and "ABS" in code:
                    if state > 0:
                        key_state = code + "+"
                    elif state < 0:
                        key_state = code + "-"
                    event_info["key"] = KEYS[key_state]
                else:
                    event_info["key"] = KEYS[code]

        return event_info


if __name__ == "__main__":
    gi = GamepadInputter()
    for _ in range(50):
        print(gi.run_event())
