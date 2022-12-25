from datetime import datetime

from utils import create_folder, list_files, printer, write_file


class PostwrittenScripter:
    """This records the commands that are being executed by a DroneControl object.

    Post in 'PostwrittenScripter' means written after the command has been executed.
    Format of commands script is:
        # example.txt
        THROTTLE_DECR 24
        YAW_INCR PITCH_INCR 30
        ROLL_INCR 23

    NB: A command can has one or two command types. When two, it means both left and right joysticks have been pressed
    simultaneously. The number at the end is the number of times it should run for.

    Attributes:
        *script: A list of the commands that are being executed by a DroneControl object.
        *control_values: Stores the current values of the DroneControl object being monitored.
        *gradient: Stores the change in the four fundamental controls (i.e. THROTTLE, YAW etc.) of
        the DroneControl object per any new event.
        *mag_dir: This stores the magnitude and direction of the current command being executed. It resets
        with a change in gradient.
    """

    CTRLS = "THROTTLE", "YAW", "PITCH", "ROLL"
    SCRIPTING_ROOT_PATH = "scriptings/postwritten"

    def __init__(self) -> None:
        self.check_default_path()
        self.script = []
        self.mag_dir = {c: 0 for c in self.CTRLS}
        self.gradient = {c: 0 for c in self.CTRLS}
        self.control_values = {c: 0 for c in self.CTRLS}

    def check_default_path(self):
        """Checks if path to which scripts (.txt) files are to be saved exists."""

        create_folder(self.SCRIPTING_ROOT_PATH)

    def list_scripts(self):
        """List filenames that are in postwritten scripts folder."""

        return list_files(self.SCRIPTING_ROOT_PATH)

    def reset_mag_dir(self) -> None:
        """Resets magnitude and direction to zero."""

        self.mag_dir = {c: 0 for c in self.CTRLS}

    def update_mag_dir(self) -> None:
        """Updates magnitude and direction with gradient values."""

        for c in self.CTRLS:
            self.mag_dir[c] += self.gradient[c]

    def calc_gradient(self, new_control_values: dict) -> dict:
        """Calculates difference in new controls values and current contorl values."""

        grad = {c: new_control_values[c] - self.control_values[c] for c in self.CTRLS}
        return grad

    def is_zero_gradient(self) -> bool:
        """Check if gradient is zero i.e. no change in control values."""

        return sum(list(self.gradient.values())) == 0

    def check_event(self, new_control_values: dict) -> None:
        """Updates the script with a command.

        Checks to see there is a change in gradient. If so,  add the command to the list of commands stored in 'script'.
        Then, reset magnitiude and direction of current command. Perform updates to gradient.

        Args:
            *new_control_values: A dict containing the next state control values of the DroneControl object being monitored.
        """

        grad = self.calc_gradient(new_control_values)

        # Check for change in gradient
        if self.gradient == grad or self.is_zero_gradient():
            self.update_mag_dir()

        else:
            self.add_script_line()
            self.reset_mag_dir()

        self.gradient = grad
        self.control_values = new_control_values

    def add_script_line(self) -> None:
        """Adds current command to list of commands being recorded in 'script'."""

        line = ""
        mag_vals = set(self.mag_dir.values())
        mag = None

        for k in self.mag_dir:
            # Check for direction and record magnitude in that direction
            if self.mag_dir[k] > 0:
                line += k + "_INCR "
                mag = max(mag_vals)
            elif self.mag_dir[k] < 0:
                line += k + "_DECR "
                mag = abs(min(mag_vals))

        if mag:
            line += str(mag)
        if line:
            print(f"-> {line}")
            self.script.append(line)

    def postwritten_script_writer(self) -> None:
        """Saves script currently recorded into a .txt file."""

        if self.script:
            now = datetime.now()
            filename = (
                f"{now.year}{now.month}{now.day}_{now.hour}{now.minute}{now.second}"
            )

            write_file(
                folder_path=self.SCRIPTING_ROOT_PATH,
                file_contents=self.script,
                filename=filename,
            )
            self.script = []  # Reset 'script'

            print("----------------------------")
            print()
            print(f"Script saved at {filename}.txt")
            print()
            print("----------------------------")


if __name__ == "__main__":
    p = PostwrittenScripter()
    p.postwritten_script_writer()
