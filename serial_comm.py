import time

import serial
import serial.tools.list_ports

from drone_controller import DroneController


class SerialComm:
    def __init__(self) -> None:
        self.com_port = ""
        self.get_Arduino_port()
        self.baud_rate = 9600
        self.Arduino = None
        self.set_Arduino()

    def set_Arduino(self):
        if self.com_port:
            self.Arduino = serial.Serial(
                self.com_port, self.baud_rate, write_timeout=0.01
            )
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


if __name__ == "__main__":
    cntrllr = DroneController()
    s = SerialComm()

    while not cntrllr.exit:
        vals = cntrllr.run_event()
        comm_str = ""
        comm_list = [i + 200 for i in vals.values()]
        data_bytes = bytes(comm_list)

        print(comm_list)

        s.Arduino.write(data_bytes)
        time.sleep(0.1)
        s.Arduino.flush()
