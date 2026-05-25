import serial
import time

SERIAL_PORT = "/dev/cu.usbserial-0001"
BAUD_RATE = 115200

print("Connecting to ESP32...")

ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)

time.sleep(2)

print("Connected! Reading sensor data...\n")

while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode("utf-8").strip()
        print(line)