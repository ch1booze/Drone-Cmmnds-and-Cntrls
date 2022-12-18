from drone_controls import DroneControls
from gamepad_inputter import GamepadInputter
from gamepad_mapping import GAMEPAD_MAPPING
from keyboard_inputter import KeyboardInputter
from keyboard_mapping import KEYBOARD_MAPPING
from postwritten_scripter import PostwrittenScripter
from prewritten_scripter import PrewrittenScripter
from script_executor import ScriptExecutor
from state_manager import StateManager
from mapping import Mapping


class DroneNet:
    DEVICES = "KYBD", "GMPD"

    def __init__(self) -> None:
        self.gmpd_inpttr = GamepadInputter()
        self.gmpd_mppng = Mapping(GAMEPAD_MAPPING)
        self.gmpd_state_mngr = StateManager(GAMEPAD_MAPPING)

        self.kybd_inpttr = KeyboardInputter()
        self.kybd_mppng = Mapping(KEYBOARD_MAPPING)
        self.kybd_state_mngr = StateManager(KEYBOARD_MAPPING)

        self.controls = DroneControls()

        # self.scrpt_exe = ScriptExecutor()
        self.prewrttn_scrptr = PrewrittenScripter()
        self.pstwrttn_scrptr = PostwrittenScripter()

        self.armed = None
        self.disarm()
        self.input_device = self.DEVICES[0]
        self.exit = False

    def arm(self):
        self.armed = True
        print("Drone armed")

    def disarm(self):
        self.armed = False
        print("Drone disarmed")

    def run(self):
        if self.input_device == self.DEVICES[0]:
            self.kybd_control()
        elif self.input_device == self.DEVICES[1]:
            self.gmpd_control()

    def kybd_control(self):
        event_info = self.kybd_inpttr.run_event()
        if event_info:
            print(f"Event: {event_info}")

            if event_info["key"] == "ctrl+h":
                self.input_device = self.DEVICES[1]

            elif event_info["key"] == "ctrl+p":
                self.prewrttn_scrptr.prewritten_script_writer()

            elif event_info["key"] == "ctrl+e":
                self.arm()

            elif event_info["key"] == "ctrl+q":
                self.disarm()
                self.pstwrttn_scrptr.postwritten_script_writer()

            elif event_info["key"] == "ctrl+x":
                self.exit = True

            else:
                if self.armed:
                    self.kybd_state_mngr.run(event_info)
                    left_js, right_js = self.kybd_state_mngr.get_js()
                    states = self.kybd_state_mngr.get_states()

                    print(f"JS: {left_js, right_js}")

                    left_js_action = self.kybd_mppng.get_action(left_js)
                    right_js_action = self.kybd_mppng.get_action(right_js)
                    self.controls.reset(states)

                    if left_js_action:
                        self.controls.get_outcome(left_js_action)

                    if right_js_action:
                        self.controls.get_outcome(right_js_action)

                    vals = self.controls.get_values()
                    print(f"Values: {vals})")

                    self.pstwrttn_scrptr.check_event(vals)
                    print(f"Script: {self.pstwrttn_scrptr.script}")
                    print("----------------------")

    def gmpd_control(self):
        event_info = self.kybd_inpttr.run_event(event_info)
        if event_info:
            print(f"Event: {event_info}")

            if event_info["key"] == "Select":
                self.input_device = self.DEVICES[0]

            else:
                if self.armed:
                    self.gmpd_state_mngr.run()
                    left_js, right_js = self.kybd_state_mngr.get_js()
                    states = self.kybd_state_mngr.get_states()

                    print(f"JS: {left_js, right_js}")

                    left_js_action = self.kybd_mppng.get_action(left_js)
                    right_js_action = self.kybd_mppng.get_action(right_js)
                    self.controls.reset(states)

                    if left_js_action:
                        self.controls.get_outcome(left_js_action)

                    if right_js_action:
                        self.controls.get_outcome(right_js_action)

                    vals = self.controls.get_values()
                    print(f"Values: {vals})")

                    self.pstwrttn_scrptr.check_event(vals)
                    print(f"Script: {self.pstwrttn_scrptr.script}")
                    print("----------------------")


if __name__ == "__main__":
    drone = DroneNet()
    while True:
        if drone.exit:
            break
        else:
            drone.run()
