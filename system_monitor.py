import psutil
import time
from datetime import datetime
while True:
    print("=== SYSTEM HEALTH MONITOR ===")
    current_time = datetime.now()
    print("Check Time:", current_time.strftime("%d-%m-%Y %H:%M:%S"))
    cpu_usage= psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")
    ram_usage= psutil.virtual_memory().percent
    print(f"RAM Usage: {ram_usage}%")
    disk_usage= psutil.disk_usage("C:\\").percent
    print(f"DISK Usage: {disk_usage}%")
    if cpu_usage >= 80:
        print("WARNING: High CPU Usage!")
    else:
        print("CPU Status: Normal")

    if ram_usage >= 80:
        print("WARNING: High RAM Usage!")
    else:
        print("RAM Status: Normal")
    if disk_usage >= 90:
        print("WARNING: High Disk Usage!")
    else:
        print("Disk Status: Normal") 
    time.sleep(60)   