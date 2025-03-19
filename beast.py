import os
import time
import psutil
import shutil
import subprocess

def is_process_running(process_name):
    """Check if a process is running."""
    for proc in psutil.process_iter(['name']):
        try:
            if process_name.lower() in proc.info['name'].lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def restart_process(exe_path):
    """Restart a process if not running."""
    if not is_process_running(os.path.basename(exe_path)):
        subprocess.Popen(exe_path, shell=True)
        time.sleep(2)  # Small delay to ensure it launches

def lock_file(path):
    """Make a file undeletable."""
    os.system(f'icacls "{path}" /deny Everyone:(DE,WDAC)')

def main():
    # Paths to blocker and watchdog
    blocker_path = r"C:\Users\Kusal Darshana\Documents\blocker\dist\blocker.exe"
    watchdog_path = r"C:\Users\Kusal Darshana\Documents\blocker\dist\watchdog.exe"
    backup_folder = r"C:\Program Files (x86)\Common Files\Microsoft\ExtensionManager\Extensions\Microsoft\Windows Kits\10\Desktop SDK"
    os.makedirs(backup_folder, exist_ok=True)
    
    # Backup copies
    if not os.path.exists(backup_folder + "blocker.exe"):
        shutil.copy(blocker_path, backup_folder + "blocker.exe")
    if not os.path.exists(backup_folder + "watchdog.exe"):
        shutil.copy(watchdog_path, backup_folder + "watchdog.exe")
    
    # Lock down the files
    lock_file(blocker_path)
    lock_file(watchdog_path)
    
    while True:
        # Restart watchdog if missing
        if not os.path.exists(watchdog_path):
            shutil.copy(backup_folder + "watchdog.exe", watchdog_path)
            restart_process(watchdog_path)
            lock_file(watchdog_path)
        
        # Restart blocker if missing
        if not os.path.exists(blocker_path):
            shutil.copy(backup_folder + "blocker.exe", blocker_path)
            restart_process(blocker_path)
            lock_file(blocker_path)
        
        # If both are missing, force restart the system
        if not os.path.exists(blocker_path) and not os.path.exists(watchdog_path):
            os.system("shutdown /r /t 10")  # Restart PC in 10 sec 😈
            break
        
        time.sleep(5)  # Check every 5 seconds

if __name__ == "__main__":
    main()
