import os
import platform
import psutil
import time
from datetime import datetime

# Change names to log files
log_files = {
    'network': 'network_activity_log.txt',
    'disk_io': 'disk_io_log.txt',
    'system_load': 'system_load_log.txt',
    'process': 'process_log.txt'
}

# In seconds!!
intervals = {
    'network': 100,  # Interval in seconds
    'disk_io': 1000,  # Interval for disk input/output
    'system_load': 60,  # Interval for System Overloads
    'process': 60  # Interval for proc monitoring
}

# Список процесів, які не потрібно відслідковувати
excluded_processes = {"explorer.exe", "svchost.exe", "System Idle Process"}


# Моніторинг мережевої активності
def log_network_activity():
    with open(log_files['network'], 'a') as f:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(f"----- {timestamp} -----\n")

        for conn in psutil.net_connections(kind='inet'):
            f.write(f"Network Connection: {conn.laddr} -> {conn.raddr} (Status: {conn.status})\n")

        f.write("\n")


# Disk input
def log_disk_io():
    with open(log_files['disk_io'], 'a') as f:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(f"----- {timestamp} -----\n")

        try:
            for disk in psutil.disk_partitions():
                try:
                    usage = psutil.disk_usage(disk.mountpoint)
                    io_counters = psutil.disk_io_counters(perdisk=True).get(disk.device, None)
                    if io_counters:
                        f.write(f"Disk: {disk.device}\n")
                        f.write(f"  Total Read: {io_counters.read_bytes / (1024 * 1024):.2f} MB\n")
                        f.write(f"  Total Write: {io_counters.write_bytes / (1024 * 1024):.2f} MB\n")
                        f.write(f"  Disk Usage: {usage.percent}%\n")
                        f.write(f"  Used Space: {usage.used / (1024 * 1024):.2f} MB\n")
                        f.write(f"  Total Space: {usage.total / (1024 * 1024):.2f} MB\n")
                except PermissionError as e:
                    f.write(f"PermissionError accessing disk {disk.device}: {e}\n")
                except FileNotFoundError as e:
                    f.write(f"FileNotFoundError accessing disk {disk.device}: {e}\n")

        except Exception as e:
            f.write(f"Error accessing disk partitions: {e}\n")

        f.write("\n")

#Computer Overload
def log_system_load():
    with open(log_files['system_load'], 'a') as f:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(f"----- {timestamp} -----\n")

        cpu_usage = psutil.cpu_percent(interval=1)
        f.write(f"CPU Usage: {cpu_usage}%\n")

        memory_info = psutil.virtual_memory()
        f.write(f"Memory Usage: {memory_info.percent}%\n")
        f.write(f"Available Memory: {memory_info.available / (1024 * 1024):.2f} MB\n")

        disk_usage = psutil.disk_usage('/')
        f.write(f"Disk Usage: {disk_usage.percent}%\n")
        f.write(f"Available Disk Space: {disk_usage.free / (1024 * 1024):.2f} MB\n")

        f.write("\n")

def log_processes():
    with open(log_files['process'], 'a') as f:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(f"----- {timestamp} -----\n")

        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] not in excluded_processes:
                f.write(f"Process: PID={proc.info['pid']}, Name={proc.info['name']}\n")

        f.write("\n")


def main():
    image = [
"       ___________________                      ___     ___            ",
"     /                    \                    /   \___/   \           ",
"    |  _________________   |                  |  O       O  |          ",
"    | |                 |  |                  |      V      |          ",
"    | |  $ sudo check   |  |                   \    ___    /           ",
"    | |  Checking...    |  |                    \_________/            ",
"    | |  Status:[ OK? ] |  |                                           ",
"    | |_________________|  |                      MoniTrack            ",
"    |______________________|                                           ",
"           /       \                     automatic monitoring script   ",
"          /         \                            version 1.0           ",
"         |___________|                        by Bohdan Misonh         "
    ]
    for line in image:
        print(line)
        time.sleep(0.2)  

    print(" ")
    print("Starting...")
    print("--------------------------------------------------------------------")
    
    next_check_times = {
        'network': time.time(),
        'disk_io': time.time(),
        'system_load': time.time(),
        'process': time.time()
    }

    while True:
        current_time = time.time()

        if current_time >= next_check_times['network']:
            log_network_activity()
            next_check_times['network'] = current_time + intervals['network']

        if current_time >= next_check_times['disk_io']:
            log_disk_io()
            next_check_times['disk_io'] = current_time + intervals['disk_io']

        if current_time >= next_check_times['system_load']:
            log_system_load()
            next_check_times['system_load'] = current_time + intervals['system_load']

        if current_time >= next_check_times['process']:
            log_processes()
            next_check_times['process'] = current_time + intervals['process']

        time.sleep(1)


if __name__ == "__main__":
    main()
