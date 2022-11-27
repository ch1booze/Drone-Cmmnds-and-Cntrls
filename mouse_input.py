from pynput import mouse

class MouseInput:
    def __init__(self) -> None:
        self.event_catcher = mouse.Events()
        self.event_catcher.start()


    def get_event(self):
        event = self.event_catcher.get()
        return event


mse = MouseInput()
for _ in range(75):
    print(mse.get_event())
