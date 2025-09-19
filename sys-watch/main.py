import psutil
import shutil
import json

from datetime import datetime

def get_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    return cpu_usage

def get_memory_usage():
    memory = psutil.virtual_memory()
    return memory.percent

def get_disk_usage():
    disk = shutil.disk_usage("/")

    used_percentage = (disk.used / disk.total) * 100

    return round(used_percentage, 2)

def get_boot_time():
    boot_time = datetime.fromtimestamp(psutil.boot_time())

    formatted_time = boot_time.strftime("%Y-%m-%d %H:%M:%S")

    return formatted_time

def get_top_processes():
    processes = []

    for process in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            processes.append(process.info)

        except:
            pass

    top_processes = sorted(
        processes,
        key=lambda process: process['cpu_percent'],
        reverse=True
    )[:5]

    return top_processes

def export_report(system_data):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"logs/report_{timestamp}.json"

    with open(filename, "w") as file:
        json.dump(system_data, file, indent=4)

    print(f"\nSystem report exported to: {filename}")

system_data = {
    "cpu_usage": get_cpu_usage(),
    "memory_usage": get_memory_usage(),
    "disk_usage": get_disk_usage(),
    "boot_time": get_boot_time(),
    "top_processes": get_top_processes()
}

print("\n========== SYS WATCH ==========\n")

print(f"CPU Usage      : {system_data['cpu_usage']}%")
print(f"Memory Usage   : {system_data['memory_usage']}%")
print(f"Disk Usage     : {system_data['disk_usage']}%")
print(f"System Booted  : {system_data['boot_time']}")

print("\nTop Processes:\n")

for process in system_data['top_processes']:
    print(
        f"PID: {process['pid']} | "
        f"Name: {process['name']} | "
        f"CPU: {process['cpu_percent']}%"
    )

export_report(system_data)

print("\n===============================\n")