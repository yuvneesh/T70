import serial.tools.list_ports

ports = list(serial.tools.list_ports.comports())
for port in ports:
    try:
        ser = serial.Serial(port.device)
        ser.close()
        print("Port {} is free to use.".format(port.device))
    except (OSError, serial.SerialException):
        print("Port {} is already in use.".format(port.device))
