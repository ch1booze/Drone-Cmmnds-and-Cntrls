import time

import serial
import serial.tools.list_ports


class SerialComm:
    def __init__(self) -> None:
        self.com_port = ""
        self.get_Arduino_port()
        self.baud_rate = 115200
        self.Arduino = None
        self.set_Arduino()

    def set_Arduino(self):
        if self.com_port:
            self.Arduino = serial.Serial(self.com_port, self.baud_rate)
            print("Arduino found!")

    def get_Arduino_port(self):
        ports = serial.tools.list_ports.comports()
        com_port = ""
        print(ports)
        for port in ports:
            port_str = str(port)
            print(port_str)
            if "Arduino" in port_str or "CH340" in port_str:
                com_port = port_str.split()[0]
                break

        if com_port:
            self.com_port = com_port
        else:
            print("Arduino not found!")

    def send_Arduino_data(self, data: str) -> None:
        cmd_str = f"{data}\r"
        print(cmd_str)
        self.Arduino.write(cmd_str.encode())
        time.sleep(1)


if __name__ == "__main__":
    from random import randint

    s = SerialComm()
    while True:
        for i in range(15):
            cmd = ""
            for _ in range(4):
                # cmd += str(randint(0, 400)).zfill(3)
                if i < 3:
                    cmd += "100"
                elif i < 6:
                    cmd += "200"
                elif i < 9:
                    cmd += "300"
                else:
                    cmd += "400"

            s.send_Arduino_data(cmd)

        break
