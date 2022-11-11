class BaseControl:
    def __init__(self, magnitude, rate_of_change) -> None:
        self.magnitude = magnitude
        self.rate_of_change = rate_of_change
        self.value = 0

    def increase(self):
        if self.value + self.rate_of_change <= self.magnitude:
            self.value += self.rate_of_change

    def decrease(self):
        if self.value - self.rate_of_change >= -self.magnitude:
            self.value -= self.rate_of_change

    def reset_value(self):
        self.value = 0

    def get_value(self):
        return self.value
