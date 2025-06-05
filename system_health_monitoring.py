import psutil
import logging

# Set threshold values
CPU_THRESHOLD = 80  # in percent
MEMORY_THRESHOLD = 80  # in percent
DISK_THRESHOLD = 90  # in percent

# Setup logging
logging.basicConfig(filename="system_health.log", level=logging.INFO, format="%(asctime)s - %(message)s")

def check_system_health():
    alerts = []

    # CPU usage
    cpu = psutil.cpu_percent(interval=1)
    if cpu > CPU_THRESHOLD:
        alerts.append(f"High CPU usage: {cpu}%")

    # Memory usage
    memory = psutil.virtual_memory().percent
    if memory > MEMORY_THRESHOLD:
        alerts.append(f"High Memory usage: {memory}%")

    # Disk usage
    disk = psutil.disk_usage('/').percent
    if disk > DISK_THRESHOLD:
        alerts.append(f"High Disk usage: {disk}%")

    # Running processes
    processes = len(psutil.pids())
    alerts.append(f"Total running processes: {processes}")

    if alerts:
        for alert in alerts:
            print(alert)
            logging.info(alert)
    else:
        print("System is healthy.")
        logging.info("System is healthy.")

check_system_health()
