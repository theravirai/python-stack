import psutil

def get_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    return cpu_usage

print("\n===== SYS WATCH =====\n")

cpu = get_cpu_usage()

print(f"CPU Usage: {cpu}%")
