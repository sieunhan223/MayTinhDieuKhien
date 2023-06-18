import serial

def DeviceConnect(port, baurate):
    ser = serial.Serial(port,baurate, write_timeout=2)
    print("UART: ",ser.is_open)
    return ser
def Mode0(ser):
    ser.write(b"0")
def Mode1(ser):
    ser.write(b"1")
def Mode2(ser):
    ser.write(b"2")