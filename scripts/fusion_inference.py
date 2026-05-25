import cv2
import serial
import time
import numpy as np

# =========================
# SERIAL CONNECTION TO ESP32
# =========================
SERIAL_PORT = "/dev/cu.usbserial-0001"
BAUD_RATE = 115200

print("Connecting to ESP32...")

ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)

time.sleep(2)

print("Connected to ESP32")

# =========================
# OPEN WEBCAM
# =========================
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()

# =========================
# SENSOR VARIABLES
# =========================
temperature = "N/A"
humidity = "N/A"

# =========================
# MAIN LOOP
# =========================
while True:

    # -------------------------
    # READ CAMERA FRAME
    # -------------------------
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break

    # -------------------------
    # READ SERIAL DATA
    # -------------------------
    while ser.in_waiting > 0:

        line = ser.readline().decode("utf-8").strip()

        print("ESP32:", line)

        # Parse temperature
        if "Temperature:" in line:
            temperature = line.split(":")[1].strip()

        # Parse humidity
        elif "Humidity:" in line:
            humidity = line.split(":")[1].strip()

    # -------------------------
    # CONVERT TO HSV
    # -------------------------
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # -------------------------
    # GREEN COLOR RANGE
    # -------------------------
    lower_green = np.array([35, 40, 40])
    upper_green = np.array([90, 255, 255])

    # -------------------------
    # CREATE GREEN MASK
    # -------------------------
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # -------------------------
    # COUNT GREEN PIXELS
    # -------------------------
    green_pixels = cv2.countNonZero(mask)

    # -------------------------
    # PLANT HEALTH LOGIC
    # -------------------------
    if green_pixels > 3000:
        plant_status = "HEALTHY"
        status_color = (0, 255, 0)

    elif green_pixels > 1000:
        plant_status = "MODERATE GREEN"
        status_color = (0, 255, 255)

    else:
        plant_status = "LOW GREEN DETECTED"
        status_color = (0, 0, 255)

    # -------------------------
    # DISPLAY TEMPERATURE
    # -------------------------
    cv2.putText(
        frame,
        f"Temperature: {temperature}",
        (10, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # -------------------------
    # DISPLAY HUMIDITY
    # -------------------------
    cv2.putText(
        frame,
        f"Humidity: {humidity}",
        (10, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 0, 0),
        2
    )

    # -------------------------
    # DISPLAY GREEN PIXELS
    # -------------------------
    cv2.putText(
        frame,
        f"Green Pixels: {green_pixels}",
        (10, 120),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 255),
        2
    )

    # -------------------------
    # DISPLAY STATUS
    # -------------------------
    cv2.putText(
        frame,
        f"Plant Status: {plant_status}",
        (10, 170),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        status_color,
        2
    )

    # -------------------------
    # SHOW WINDOW
    # -------------------------
    cv2.imshow("Plant Health Multimodal AI", frame)

    # -------------------------
    # PRESS Q TO QUIT
    # -------------------------
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# =========================
# CLEANUP
# =========================
cap.release()
cv2.destroyAllWindows()
ser.close()

print("Program ended")