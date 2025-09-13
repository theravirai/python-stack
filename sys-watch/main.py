import psutil

def get_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    return cpu_usage

def get_memory_usage():
    memory = psutil.virtual_memory()
    return memory.percent

print("\n===== SYS WATCH =====\n")

cpu = get_cpu_usage()
memory = get_memory_usage()

print(f"CPU Usage: {cpu}%")
print(f"Memory Usage: {memory}%")
