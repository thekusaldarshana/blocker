import time
import psutil
import subprocess

# Function to check if blocker.exe is running
def is_blocker_running():
    for proc in psutil.process_iter(['name']):
        try:
            if proc.info['name'].lower() == "blocker.exe":
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

# Function to restart blocker.exe if it's not running
def restart_blocker():
    blocker_path = r"C:\Users\Kusal Darshana\Documents\blocker\dist\blocker.exe"  # Adjust the path if needed
    print("🚀 Blocker is not running! Restarting now...")
    subprocess.Popen([blocker_path], shell=True)

# Continuous monitoring
while True:
    if not is_blocker_running():
        restart_blocker()
    
    time.sleep(5)  # Check every 5 seconds
