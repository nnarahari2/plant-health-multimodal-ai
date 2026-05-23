import cv2
import os

# Load image
image_path = "data/images/test_plant.jpg"
import cv2

print("Starting live webcam inference...")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame.")
        break

    cv2.imshow("Plant Health Webcam", frame)

    # Press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()