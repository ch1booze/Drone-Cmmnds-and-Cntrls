from pynput import keyboard as kb
from pynput import mouse as ms

a = 0
b = 0

with kb.Events() as events:
    for event in events:
        if event.key == kb.Key.backspace:
            a += 1
            print(f"a: {a}")
        elif event.key == kb.Key.alt:
            b += 1
            print(f"b: {b}")
        elif event.key == kb.Key.end:
            b += 1
            print(f"b: {b}")
        else:
            print("Just another key has been pressed!")
        

