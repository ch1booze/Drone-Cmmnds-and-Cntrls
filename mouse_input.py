from pynput import mouse


def button_side(button):
    if button == mouse.Button.left:
        return "LEFT"
    elif button == mouse.Button.right:
        return "RGHT"


def scroll_direction(scroll):
    if scroll.dy == 1:
        return "UP"
    elif scroll.dy == -1:
        return "DN"


class MouseInput:
    EVENT_CLICK = mouse.Events.Click
    EVENT_SCROLL = mouse.Events.Scroll

    def __init__(self) -> None:
        self.event_catcher = mouse.Events()
        self.event_catcher.start()

    def get_event(self):
        event = self.event_catcher.get()
        return event

    def event_handler(self, event):
        event_info = None
        if type(event) == self.EVENT_CLICK:
            event_type = "CLCK"
            event_button = button_side(event.button)
            event_pressed = event.pressed
            event_info = event_button + "_" + event_type, event_pressed

        elif type(event) == self.EVENT_SCROLL:
            event_type = "SCRL"
            event_change = scroll_direction(event)
            event_info = event_type + "_" + event_change

        return event_info

    def run(self):
        event = self.get_event()
        event_info = self.event_handler(event)

        return event_info


if __name__ == "__main__":
    m = MouseInput()
    for _ in range(50):
        print(m.run())
