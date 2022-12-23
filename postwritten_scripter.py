from utils import create_folder, list_files, printer


class PostwrittenScripter:
    """This records the commands that are being executed by a DroneControl object.

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
        """"""
        create_folder(self.SCRIPTING_ROOT_PATH)

    def list_scripts(self):
        return list_files(self.SCRIPTING_ROOT_PATH)

    def get_script(self):
        return self.script

    def reset_mag_dir(self):
        self.mag_dir = {c: 0 for c in self.CTRLS}

    def update_mag_dir(self) -> None:
        for c in self.CTRLS:
            self.mag_dir[c] += self.gradient[c]

    def calc_gradient(self, new_control_values: dict) -> dict:
        grad = {c: new_control_values[c] - self.control_values[c] for c in self.CTRLS}

        return grad

    def is_zero_gradient(self) -> bool:
        return sum(list(self.gradient.values())) == 0

    def check_event(self, new_control_values: dict) -> None:
        grad = self.calc_gradient(new_control_values)

        if self.gradient == grad or self.is_zero_gradient():
            self.update_mag_dir()

        else:
            self.add_script_line()
            self.reset_mag_dir()

        self.gradient = grad
        self.control_values = new_control_values
        print(f"Grad: {self.gradient}")

    def add_script_line(self) -> None:
        line = ""
        mag_vals = set(self.mag_dir.values())
        mag = None

        for k in self.mag_dir:
            if self.mag_dir[k] > 0:
                line += k + "_INCR "
                mag = max(mag_vals)
            elif self.mag_dir[k] < 0:
                line += k + "_DECR "
                mag = abs(min(mag_vals))

        if mag:
            line += str(mag)
        if line:
            self.script.append(line)

    def postwritten_script_writer(self) -> None:
        if self.script:
            printer(f"Scripts: {self.list_scripts()}")
            filename = input("Enter filename: ")

            write_file(
                folder_path=self.SCRIPTING_ROOT_PATH,
                file_contents=self.script,
                filename=filename,
            )
