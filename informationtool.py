import subprocess

cpu_info = subprocess.check_output("lscpu", shell=True).decode()
mem_info = subprocess.check_output("free -h", shell=True).decode()
disk_info = subprocess.check_output("df -h", shell=True).decode()

for line in cpu_info.splitlines():
     if "Model name" in line:
      parts = line.split(":", 1)
print(parts[0].strip() + ": " + parts[1].strip())


for line in mem_info.splitlines():
   if "Memory" in line:
      print(line)



# def get_system_info():
   

#     # return f"CPU Information:\n{cpu_info}\nMemory Information:\n{mem_info}\nDisk Information:\n{disk_info}"
    


# print(get_system_info())


