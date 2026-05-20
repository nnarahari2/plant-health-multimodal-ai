import pandas as pd
import random
import os

image_folder = "data/images"

rows = []

for root, dirs, files in os.walk(image_folder):
    for file in files:
        if file.endswith((".jpg", ".png", ".jpeg")):

            rows.append({
                "image": file,
                "temperature": random.randint(18,35),
                "humidity": random.randint(30,90),
                "soil_moisture": random.randint(10,80),
                "light_level": random.randint(200,1000)
            })

df = pd.DataFrame(rows)

df.to_csv(
    "data/generated/sensor_data.csv",
    index=False
)

print("Sensor data generated.")