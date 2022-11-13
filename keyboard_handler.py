import unittest

from pynput import keyboard


class KeyboardHandler:
    COMBINATION_KEY = "\\x"
    CTRL_M = "\\r"
    SHORTCUT_KEY = "ctrl"
    PRESS = keyboard.Events.Press
    RELEASE = keyboard.Events.Release

    def get_key(self, event):
        key_string = str(event.key)
        key_string = key_string.strip("'")
        key_string = key_string.replace("_l", "")
        key_string = key_string.replace("_r", "")
        key_string = key_string.replace("Key.", "")

        return key_string

    def _char_from_num(self, key_combo):
        hex_str = key_combo.replace(self.COMBINATION_KEY, "")
        integer = int(hex_str, 16)
        if 1 <= integer <= 26:
            letter = chr(ord("a") + integer - 1)

        print(f"letter: {letter}")

        return letter

    def handler(self, event):
        if type(event) == self.PRESS:
            key = self.get_key(event)

            if self.COMBINATION_KEY in key:
                key = self.SHORTCUT_KEY + "+" + self._char_from_num(key)

            elif key == self.CTRL_M:
                key = self.SHORTCUT_KEY + "+" + "m"

            return key

        elif type(event) == self.RELEASE:
            return "reset"


class TestKeyboardHandler(unittest.TestCase):
    def test_char_from_num(self):
        hndlr = KeyboardHandler()

        for i in range(1, 27):
            char = chr(i + 96)
            result = hndlr._char_from_num(f"\\x{i:02}")
            self.assertEqual(char, result, (char, result))


if __name__ == "__main__":
    unittest.main()
