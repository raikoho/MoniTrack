# MoniTrack

**MoniTrack** - Your Ultimate System Surveillance Companion

![MoniTrack Banner](MoniTrack.png)

It is a powerful and versatile monitoring tool designed to keep an eye on your system's health, security, and performance. Whether you're a security enthusiast, system administrator, or simply a tech-savvy user, It provides comprehensive insights into your system's activities, resource usage, and potential threats.

## Features

### 🌐 Network Activity Monitoring
- **Real-time Insights**: Track active network connections, including local and remote addresses, and their statuses.
- **Detailed Logs**: Capture and log all network activities, including connection details and statuses to help identify unusual or unauthorized connections.

### 💾 Disk I/O Statistics
- **Read/Write Metrics**: Monitor the total amount of data read from and written to your disks.
- **Performance Insights**: Track read and write times, and I/O operations to evaluate disk performance.

### 🧠 System Load Overview
- **CPU Usage**: Real-time monitoring of CPU usage to ensure optimal performance.
- **Memory Usage**: Insights into available and used memory to avoid bottlenecks.
- **Disk Usage**: Track overall disk usage and available space to prevent storage issues.

### 🏃‍♂️ Process Monitoring
- **Active Processes**: List of currently running processes, excluding those marked as safe.
- **Threat Detection**: Spot potentially suspicious processes by comparing against a whitelist of known safe applications.

### 🔄 Customizable Intervals and Features
- **Flexible Monitoring**: Set custom intervals for different types of monitoring to suit your needs.
- **Define safe processes**: Set your own processes that you trust to avoid writing them to log files.

## Installation and start

   ```bash
   git clone https://github.com/raikoho/MoniTrack.git
   cd MoniTrack
   pip install -r requirements.txt
   python3 MoniTrack.py
   ```

## 🧩 Dependencies
The script uses the following modules that you should install before running (if you don't already have them):

**platform, psutil, datetime, os**

## 📜 Instruction:
Change the frequency of execution of various modules if you need. (in seconds):
```python
intervals = {
    'network': 100,  # Interval for network monitoring
    'disk_io': 1000,  # Interval for disk input/output
    'system_load': 60,  # Interval for System Overloads
    'process': 60  # Interval for proc monitoring
}
```
Reduce the list of programs by adding safe processes to the exception. 
```python
excluded_processes  = {"explorer.exe", "svchost.exe", "System Idle Process"}  # Add here more
```
Start **MoniTrack**.
You can view all saved information in the main folder with the **script**:
- **Network Activity:** View real-time network connection details in network_activity_log.txt.
- **Disk I/O Statistics:** Check disk read/write metrics and performance in disk_io_log.txt.
- **System Load:** Review CPU, memory, and disk usage statistics in system_load_log.txt.
- **Processes:** Analyze active processes and detect potential threats in process_log.txt.
