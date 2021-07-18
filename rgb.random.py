import serial                 
import random
import time
ser = serial.Serial("COM10", "9600", timeout=0, parity=serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE , bytesize = serial.EIGHTBITS, rtscts=0)


while True: 
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
    time.sleep(0.2)
