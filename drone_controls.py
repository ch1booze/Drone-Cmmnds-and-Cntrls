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
            "RESET": self.reset
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

    def reset(self):
        self.throttle.reset_value()
        self.yaw.reset_value()
        self.pitch.reset_value()
        self.roll.reset_value()
