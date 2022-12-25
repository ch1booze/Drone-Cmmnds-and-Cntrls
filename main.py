import time

from drone_controls import DroneControls
from gamepad_inputter import GamepadInputter
from gamepad_mapping import GAMEPAD_MAPPING
from keyboard_inputter import KeyboardInputter
from keyboard_mapping import KEYBOARD_MAPPING
from mapping import Mapping
from postwritten_scripter import PostwrittenScripter
from prewritten_scripter import PrewrittenScripter
from script_file_reader import ScriptFileReader
from state_manager import StateManager
from utils import printer


class DroneController:
    """This combines both gamepad and keyboard devices as inputs to be used as controller to a drone.

    Attributes:
        *controls: A DroneControls object.

        Gamepad:
            *gmpd_inpttr: A GamepadInputter object.
            *gmpd_mppng: A Mapping object set with a dict with gamepad related commands.
            *gmpd_state_mngr: A StateManager set with a dict for managing gamepad states

        Keyboard:
            *kybd_inpttr: A KeyboardInputter object.
            *kybd_mppng: A Mapping object set with a dict with keyboard related commands.
            *kybd_state_mngr: A StateManager set with a dict for managing keyboard states

        Script:
            *prewrttn_scrptr:
            *pstwrttn_scrptr
            *scrpt_file_rdr

        *armed: A bool monitoring whether the drone is armed or not.
        *input_device: Monitors the device from which events are read from.
        *exit: A bool that when True ends the DroneController execution.
    """

    DEVICES = "KYBD", "GMPD"

    def __init__(self) -> None:
        self.controls = DroneControls()

        # Keybaord related classes
        self.kybd_inpttr = KeyboardInputter()
        self.kybd_mppng = Mapping(KEYBOARD_MAPPING)
        self.kybd_state_mngr = StateManager(KEYBOARD_MAPPING)

        # Gamepad initialisation
        self.gmpd_mppng = Mapping(GAMEPAD_MAPPING)
        self.gmpd_state_mngr = StateManager(GAMEPAD_MAPPING)
        self.is_gamepad = self.gamepad_init()

        # Script related classes
        self.prewrttn_scrptr = PrewrittenScripter()
        self.pstwrttn_scrptr = PostwrittenScripter()
        self.scrpt_file_rdr = ScriptFileReader()

        # Drone related attributes
        self.armed = False
        self.kybd_help()
        self.input_device = self.DEVICES[0]
        self.exit = False

    def info(self):
        print("----------------------------")
        print()
        print(f"Armed: {self.armed}")
        print(f"Input device: {self.input_device}")
        print()
        print("----------------------------")

    def gamepad_init(self):
        """Initialises gamepad."""

        is_gamepad = False

        # Gamepad related classes
        try:
            self.gmpd_inpttr = GamepadInputter()
        except:
            print("Gamepad not detected.")
        else:
            is_gamepad = True

        return is_gamepad

    def arm(self):
        """Arms the drone."""

        self.armed = True
        print("Drone armed")

    def disarm(self):
        """Disarms the drone."""

        self.armed = False
        print("Drone disarmed")

    def run_event(self):
        """Selects the device which is used to control."""

        if self.input_device == self.DEVICES[0]:
            self.kybd_control()
        elif self.input_device == self.DEVICES[1]:
            self.gmpd_control()

    def run(self):
        while not self.exit:
            self.run_event()

    def kybd_control(self):
        """Handles functions associated with using the keyboard as an input device.

        Also executes shortcut commands used to execute script related functions, arm, disarm,
        and exit.
        """

        event_info = self.kybd_inpttr.run_event()
        if event_info:
            # SHORTCUTS COMMANDS
            # Arming the drone controller
            if event_info["key"] == "ctrl+a" and event_info["type"] == "PRSS":
                self.arm()

            # Executing a script
            elif event_info["key"] == "ctrl+e" and event_info["type"] == "PRSS":
                script = self.scrpt_file_rdr.get_file_contents()
                self.script_executor(script)

            # Displaying keyboard help information
            elif event_info["key"] == "ctrl+h" and event_info["type"] == "PRSS":
                self.kybd_help()

            # Information
            elif event_info["key"] == "ctrl+j" and event_info["type"] == "PRSS":
                self.info()

            # Recording of prewritten scripts
            elif event_info["key"] == "ctrl+p" and event_info["type"] == "PRSS":
                self.prewrttn_scrptr.prewritten_script_writer()

            # Disarming and saving postwritten scripts
            elif event_info["key"] == "ctrl+q" and event_info["type"] == "PRSS":
                self.disarm()
                self.pstwrttn_scrptr.postwritten_script_writer()

            # Switching to using gamepad as input device.
            elif event_info["key"] == "ctrl+s" and event_info["type"] == "PRSS":
                if self.gamepad_init():
                    self.gmpd_help()
                    self.input_device = self.DEVICES[1]

            # Exiting
            elif event_info["key"] == "ctrl+x" and event_info["type"] == "PRSS":
                print("Exiting...")
                time.sleep(2)
                self.exit = True

            # NORMAL COMMANDS
            else:
                if self.armed:
                    self.kybd_state_mngr.run(event_info)
                    left_js, right_js = self.kybd_state_mngr.get_js()
                    states = self.kybd_state_mngr.get_states()

                    left_js_action = self.kybd_mppng.get_action(left_js)
                    right_js_action = self.kybd_mppng.get_action(right_js)
                    self.controls.reset(states)

                    if left_js_action is not None:
                        self.controls.get_outcome(left_js_action)

                    if right_js_action is not None:
                        self.controls.get_outcome(right_js_action)

                    vals = self.controls.get_values()

                    self.pstwrttn_scrptr.check_event(vals)

    def gmpd_control(self):
        """Handles functions associated with using a gamepad as an input device."""

        event_info = self.gmpd_inpttr.run_event(event_info)
        if event_info:
            if event_info["key"] == "Select" and event_info["type"] == "PRSS":
                self.gmpd_help()
                self.input_device = self.DEVICES[0]

            elif event_info["key"] == "Start" and event_info["type"] == "PRSS":
                self.gmpd_help()

            else:
                if self.armed:
                    self.gmpd_state_mngr.run()
                    left_js, right_js = self.kybd_state_mngr.get_js()
                    states = self.kybd_state_mngr.get_states()


                    left_js_action = self.kybd_mppng.get_action(left_js)
                    right_js_action = self.kybd_mppng.get_action(right_js)
                    self.controls.reset(states)

                    if left_js_action:
                        self.controls.get_outcome(left_js_action)

                    if right_js_action:
                        self.controls.get_outcome(right_js_action)

                    vals = self.controls.get_values()

                    self.pstwrttn_scrptr.check_event(vals)

    def kybd_help(self):
        """List all instructions for how to use keyboard as input device."""

        print("----------------------------")
        print("These are controls for using the keyboard as a input device:")
        printer(KEYBOARD_MAPPING)
        print("where INCR represents increase and DECR means decrease.")
        print(
            """
Shortcut information:
    ctrl+h: Ask for help.
    ctrl+g: Gamepad initialisation
    ctrl+c: Change to input device to gamepad.
    ctrl+p: Run a PrewrittenScripter writer.
    ctrl+a: Arm.
    ctrl+q: Disarm (assumes the drone is grounded and saves the commands).
    ctrl+e: Run a script.
    ctrl+x: Exit.
        """
        )
        print("----------------------------")

    def gmpd_help(self):
        """List all the instructions for how to use gamepad as input device."""

        mppng = {k: v for k, v in GAMEPAD_MAPPING.items() if "CR" in v}

        print("----------------------------")
        print("These are controls for using a gamepad as a input device:")
        printer(mppng)
        print("where INCR represents increase and DECR means decrease.")
        print(
            """
Shortcut information:
    Start: Ask for help.
    Select: Change to input device to keyboard.
    
NB: The keyboard is considered the primary device and thus arm, disarm and other commands are to be
run using the keyboard not gamepad.
        """
        )
        print("----------------------------")

    def script_executor(self, script: list):
        """Executes commands from a script on the DroneCntrols object"""
        print("----------------------------")
        for line in script:
            print(f"-> {line}")
            script_line = line.split()
            intensity = int(script_line[-1])
            for _ in range(intensity):
                for c in script_line[:-1]:
                    self.controls.get_outcome(c)
                time.sleep(0.05)
        print("----------------------------")


if __name__ == "__main__":
    drone_cntrllr = DroneController()
    drone_cntrllr.run()
