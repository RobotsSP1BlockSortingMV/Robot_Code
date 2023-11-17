import serial
from time import sleep
import Movement as rbaction

#Method to activate the magnet and grab the object
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

#Backup method to turn the magnet off if needed
def drop_object():
    ser = serial.Serial(port='com5', baudrate=9600)
    ser.close()
    ser.open()
    ser.write(bytes.fromhex("A0 01 00 A1"))
    print('Circuit Open. Button is released')

