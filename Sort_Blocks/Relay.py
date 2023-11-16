import serial
from time import sleep
import Movement as rbaction

def grab_object():
    ser = serial.Serial(port='com5', baudrate=9600)
    ser.close()
    ser.open()
    ser.write(bytes.fromhex("A0 01 01 A2"))
    print('Circuit closed. Button is pressed')
    sleep(3)
    rbaction.movement_command('move_right_lower_shoulder',120)
    sleep(10)
    ser.write(bytes.fromhex("A0 01 00 A1"))
    print('Circuit Open. Button is released')

def drop_object():
    ser = serial.Serial(port='com5', baudrate=9600)
    ser.close()
    ser.open()
    ser.write(bytes.fromhex("A0 01 00 A1"))
    print('Circuit Open. Button is released')


#try:
 #   ser = serial.Serial(port='com5', baudrate=9600)
#    ser.close()
#    ser.open()
#    while True:
#        ser.write(bytes.fromhex("A0 01 01 A2"))
#        print('Circuit closed. Button is pressed')
#        sleep(3)
#        ser.write(bytes.fromhex("A0 01 00 A1"))
#        print('Circuit Open. Button is released')
#        sleep(3)
#except serial.SerialException as e:
#    print(f"Serial port error: {e}")
#finally:
#    ser.close()
