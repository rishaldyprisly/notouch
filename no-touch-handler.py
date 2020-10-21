import serial
import pyautogui
import time

z = pyautogui
ser = serial.Serial('COM3', 115200, timeout=1)
while (True):
    if (ser.inWaiting()>0): 
        data_str = ser.read(ser.inWaiting()).decode('utf-8') 
        print(data_str, end='')
        if 'Touch' in data_str:
            z.click(1000, 500);
        time.sleep(0.01)
