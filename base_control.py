class BaseControl:
    """This possesses all the basic functions of any of the controller inputs.

    Attributes:
        *magnitude: An int that stores the maximum a control can reach in either direction.
        *rate_of_change: An int showing the rate of change in either direction of the control.
        *value: An int for current intensity with which that control is at.
    """

    def __init__(self, magnitude: int, rate_of_change: int) -> None:
        self.magnitude = magnitude
        self.rate_of_change = rate_of_change
        self.value = 0

    def increase(self):
        """Increases the magnitude by rate of change until the limit is reached."""
        if self.value + self.rate_of_change <= self.magnitude:
            self.value += self.rate_of_change

    def decrease(self):
        """Decreases the magnitude by rate of change until the limit is reached."""
        if self.value - self.rate_of_change >= -self.magnitude:
            self.value -= self.rate_of_change

    def reset_value(self):
        self.value = 0

    def get_value(self):
        return self.value
