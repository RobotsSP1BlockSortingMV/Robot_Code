import serial
from time import sleep

try:
    ser = serial.Serial(port='com5', baudrate=9600)
    ser.close()
    ser.open()
    while True:
        ser.write(bytes.fromhex("A0 01 01 A2"))
        print('Circuit closed. Button is pressed')
        sleep(3)
        ser.write(bytes.fromhex("A0 01 00 A1"))
        print('Circuit Open. Button is released')
        sleep(3)
except serial.SerialException as e:
    print(f"Serial port error: {e}")
finally:
    ser.close()
