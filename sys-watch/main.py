import psutil
import shutil

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

print("\n===== SYS WATCH =====\n")

cpu = get_cpu_usage()
memory = get_memory_usage()
disk = get_disk_usage()

print(f"CPU Usage: {cpu}%")
print(f"Memory Usage: {memory}%")
print(f"Disk Usage: {disk}%")
