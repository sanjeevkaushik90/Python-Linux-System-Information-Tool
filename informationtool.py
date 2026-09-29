import subprocess
import socket
import getpass
import platform


def get_system_info():

    cpu_info = subprocess.check_output("lscpu", shell=True).decode()
    mem_info = subprocess.check_output("free -h", shell=True).decode()
    disk_info = subprocess.check_output("df -h", shell=True).decode()

    # CPU
    cpu = ""
    for line in cpu_info.splitlines():
        if "Model name" in line:
            parts = line.split(":", 1)
            cpu = parts[1].strip()

    # Memory
    memory = ""
    for line in mem_info.splitlines():
        if "Mem:" in line:
            parts = line.split()
            memory = parts[1]

    # Disk
    disk = ""
    for line in disk_info.splitlines():
        if "/" in line and not line.startswith("Filesystem"):
            parts = line.split()
            disk = parts[1]

    return {
        "Hostname": socket.gethostname(),
        "Operating System": platform.system(),
        "Kernel Version": platform.release(),
        "Architecture": platform.machine(),
        "CPU": cpu,
        "Memory": memory,
        "Disk": disk,
        "Current User": getpass.getuser()
    }


info = get_system_info()

print("System Information")
print("------------------")

for key, value in info.items():
    print(f"{key}: {value}")