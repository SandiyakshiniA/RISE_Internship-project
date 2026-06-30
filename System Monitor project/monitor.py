import psutil

# CPU Usage
cpu_usage = psutil.cpu_percent(interval=1)

# Memory Usage
memory = psutil.virtual_memory()

# Disk Usage
disk = psutil.disk_usage('/')

print("================================")
print("SYSTEM MONITORING REPORT")
print("================================")

print("CPU Usage:", cpu_usage, "%")
print("Memory Usage:", memory.percent, "%")
print("Disk Usage:", disk.percent, "%")

# Save Report
with open("system_report.txt", "w") as file:
    file.write("SYSTEM MONITORING REPORT\n")
    file.write("========================\n")
    file.write(f"CPU Usage: {cpu_usage}%\n")
    file.write(f"Memory Usage: {memory.percent}%\n")
    file.write(f"Disk Usage: {disk.percent}%\n")

print("\nReport Generated Successfully!")