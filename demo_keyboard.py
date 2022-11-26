from drone_controls import DroneControls
from keyboard_input import KeyboardInput
from keyboard_mapping import KeyboardMapping
from keyboard_state_manager import KeyBoardStateManager

inptter = KeyboardInput()  # reads in keyboard input
mppng = KeyboardMapping()  # maps relevant keyboard input to respective command
mapping = mppng.get_mapping()
mngr = KeyBoardStateManager(mapping)  # deciphers whether key enter is a key or key combination
cntrls = DroneControls()  # controls joystick movements

print(mapping)

while True:
    # check whether a event is a key press or release
    event_info = inptter.run()

    if event_info[0] == "q":
        break

    print(f"Event: {event_info}")

    mngr.run(event_info)  # returns key or key combo

    left_js, right_js = mngr.get_js()
    states = mngr.get_states()

    print(f"JS: {left_js, right_js}")

    left_js_action = mppng.get_action(left_js)
    right_js_action = mppng.get_action(right_js)
    cntrls.reset(states)

    if left_js_action:
        cntrls.get_outcome(left_js_action)

    if left_js_action:
        cntrls.get_outcome(right_js_action)

    print(f"Values: {cntrls.get_values()})")
    print()
