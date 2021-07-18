import win32api
import time
import random
import serial
ser = serial.Serial("COM10", "9600", timeout=0, parity=serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE , bytesize = serial.EIGHTBITS, rtscts=0)

state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
state_right = win32api.GetKeyState(0x02)  # Right button down = 0 or 1. Button up = -127 or -128

while True:
    a = win32api.GetKeyState(0x01)
    b = win32api.GetKeyState(0x02)

    if a != state_left:  # Button state changed
        state_left = a
        print(a)
        if a < 0:
            kirmizi = random.randint(0, 255)
            yesil = random.randint(0, 255)
            mavi = random.randint(0, 255)
            parlaklik = random.randint(0, 8)
            kirmizi = format(kirmizi, "03d") 
            yesil = format(yesil, "03d") 
            mavi = format(mavi, "03d") 
            parlaklik = format(parlaklik, "01d")
            veri = kirmizi + yesil + mavi + parlaklik
            print(veri)
            ser.write(veri.encode('Ascii'))
            time.sleep(0.001)