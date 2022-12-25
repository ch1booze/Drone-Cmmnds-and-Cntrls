import time

import serial.tools.list_ports
import serial


class SerialComm:
    def __init__(self) -> None:
        self.com_port = ""
        self.get_Arduino_port()
        self.baud_rate = 115200
        self.Arduino = None
        self.set_Arduino()

    def set_Arduino(self):
        if self.com_port:
            self.Arduino = serial.Serial(
                self.com_port, self.baud_rate
                )

    def get_Arduino_port(self):
        ports = serial.tools.list_ports.comports() 
        com_port = ""

        for port in ports:
            port_str = str(port)
            if "Arduino" in port_str:
                com_port = port_str.split()[0]
                break

        if com_port:
            self.com_port = com_port
        else:
            print("Arduino not found!")

    def send_Arduino_data(self, data):
        self
        self.Arduino.write(f"{data}/r".encode())

        

if __name__ == "__main__":
    ports = serial.tools.list_ports.comports() 

    print(ports)
