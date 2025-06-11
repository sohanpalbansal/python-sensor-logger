import csv
import random
import time
from datetime import datetime

filename = "temperature_log.csv"

# Write header
with open(filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Temperature (°C)"])

# Generate and log data
try:
    while True:
        temp = round(random.uniform(20.0, 40.0), 2)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(filename, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, temp])
        print(f"{timestamp} - {temp}°C logged")
        time.sleep(5)
except KeyboardInterrupt:
    print("Logging stopped.")
