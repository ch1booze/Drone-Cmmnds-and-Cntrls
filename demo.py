from drone_controls import DroneControls
from keyboard_handler import KeyboardHandler
from keyboard_input import KeyboardInput
from keyboard_mapping import KeyboardMapping

inptter = KeyboardInput()  # reads in keyboard input
hndlr = KeyboardHandler()  # deciphers whether key enter is a key or key combination
mppng = KeyboardMapping()  # maps relevant keyboard input to respective command
cntrls = DroneControls()  # controls joystick movements

while True:
    event = inptter.get_event() # check whether a key is being pressed or released
    key = hndlr.handler(event) #
    print(f"Key: {key}")

    if key == "q":
        break

    if key:
        action = mppng.get_action(key)
        print(f"Action: {action}")
        if action:
            outcome = cntrls.get_outcome(action)

    print(f"Values: {cntrls.get_values()})")
