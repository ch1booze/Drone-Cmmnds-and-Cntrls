from pynput import keyboard


class KeyboardInput:
    def __init__(self) -> None:
        self.event_catcher = keyboard.Events()
        self.event_catcher.start()

    def get_event(self):
        event = self.event_catcher.get()
        return event
