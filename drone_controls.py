from base_control import BaseControl


class DroneControls:
    MAGNITUDE = 200
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

    def get_outcome(self, inp):
        self.outcomes.get(inp, lambda: "Invalid Input")()
