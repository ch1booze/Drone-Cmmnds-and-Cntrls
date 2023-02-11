from base_control import BaseControl


class DroneControls:
    """ "This represents a drone controller with the four controls i.e. throttle, yaw, pitch, and roll.

    Attributes:
        *throttle, yaw, pitch, roll: BaseControl objects that represent controls on a drone controller.
        *outcomes: A dict of commands with their associated functions.
    """

    MAGNITUDE = 127
    RATE_OF_CHANGE = 1

    def __init__(self) -> None:
        self.throttle = BaseControl(self.MAGNITUDE, self.RATE_OF_CHANGE)
        self.yaw = BaseControl(self.MAGNITUDE, self.RATE_OF_CHANGE)
        self.pitch = BaseControl(self.MAGNITUDE, self.RATE_OF_CHANGE)
        self.roll = BaseControl(self.MAGNITUDE, self.RATE_OF_CHANGE)

        self.outcomes = None
        self.set_outcomes()

    def set_outcomes(self):
        self.outcomes = {
            "THROTTLE_INCR": self.throttle.increase,
            "THROTTLE_DECR": self.throttle.decrease,
            "YAW_INCR": self.yaw.increase,
            "YAW_DECR": self.yaw.decrease,
            "PITCH_INCR": self.pitch.increase,
            "PITCH_DECR": self.pitch.decrease,
            "ROLL_INCR": self.roll.increase,
            "ROLL_DECR": self.roll.decrease,
        }

    def get_values(self):
        values = {
            "THROTTLE": self.throttle.get_value(),
            "YAW": self.yaw.get_value(),
            "PITCH": self.pitch.get_value(),
            "ROLL": self.roll.get_value(),
        }

        return values

    def get_outcome(self, action):
        if action:
            self.outcomes.get(action)()

    def reset(self, reset_states):
        if reset_states["THROTTLE"]:
            self.throttle.reset_value()
        if reset_states["YAW"]:
            self.yaw.reset_value()
        if reset_states["PITCH"]:
            self.pitch.reset_value()
        if reset_states["ROLL"]:
            self.roll.reset_value()
