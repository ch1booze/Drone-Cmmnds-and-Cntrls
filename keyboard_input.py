from pynput import keyboard

from utils import string_stripper


class KeyboardInput:
    COMBINATION_KEY = "\\"
    SHORTCUT_KEY = "ctrl"
    PRESS = keyboard.Events.Press
    RELEASE = keyboard.Events.Release
    STRIP_LIST = ["'", "_l", "_r", "Key."]

    def __init__(self) -> None:
        self.event_catcher = keyboard.Events()
        self.event_catcher.start()

    def get_event(self):
        event = self.event_catcher.get()
        return event

    def get_key(self, event):
        key_string = str(event.key)
        key_string = string_stripper(key_string, self.STRIP_LIST)

        return key_string

    def key_combo(self, key_combo_str):
        hex_str = key_combo_str.replace(self.COMBINATION_KEY, "")
        letter = None

        if hex_str[0] == "r":
            letter = "m"
        else:
            integer = int(hex_str[1:], 16)
            if 1 <= integer <= 26:
                letter = chr(ord("a") + integer - 1)
        ky_combo_str = self.SHORTCUT_KEY + "+" + letter

        return ky_combo_str

    def event_handler(self, event):
        event_type = None
        key = self.get_key(event)

        if self.COMBINATION_KEY in key:
            key = self.key_combo(key)
            event_type = "CMBO"

        elif type(event) == self.PRESS:
            event_type = "PRSS"

        elif type(event) == self.RELEASE:
            event_type = "RLSE"

        return key, event_type

    def run(self):
        event = self.get_event()
        event_info = self.event_handler(event)

        return event_info


if __name__ == "__main__":
    inpttr = KeyboardInput()

    for _ in range(50):
        print(inpttr.run())
