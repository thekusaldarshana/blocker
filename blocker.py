import time
import psutil
import pygetwindow as gw
import subprocess

# Add your blocked words here
BLOCKED_WORDS = ["porn", "18+", "orgasm", "eporner", "pornhub", "xhasmster", "xvideo", "pornstar", "cum", "masturbate", 
"missax", "sex", "leaked", "wal", "wal katha", "walkatha", "wala", "nude", "naked", "jerk off", "වල්කතා", "වැල", 
"වල් කතා", "හුකන", "පුකේ", "හුත්ත", "වේසි", "හුකනවා", "හැමිනෙනවා", "hardcore", "erotic", "hentai", "bdsm", 
"taboo", "shemale", "camgirl", "camsex", "escort", "milf", "deepthroat", "blowjob", "handjob", "anal", "lesbian", 
"gay", "orgy", "threesome", "creampie", "dildo", "webcam sex", "onlyfans", "nsfw", "softcore", "futa", "boobs", "tits", 
"ass", "pussy", "dick", "cock", "squirting", "fingering", "pegging", "dominatrix", "mistress", "submissive", "kinky",  
"cumshot", "cuckold", "stepmom", "gay porn", "webcam girl", "stripper", "busty"]

# Function to check open browser windows
def get_browser_windows():
    browsers = ["chrome", "firefox", "edge", "opera", "brave"]
    browser_windows = []

    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if any(browser in proc.info['name'].lower() for browser in browsers):
                browser_windows.append(proc.info['pid'])
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass  # Ignore processes that are no longer active
    return browser_windows

# Function to check if blocker.exe is running
def is_process_running(process_name):
    for proc in psutil.process_iter(['name']):
        try:
            if proc.info['name'].lower() == process_name.lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

# Function to close browser if bad word is found
def close_browser():
    browser_windows = get_browser_windows()

    for window in gw.getWindowsWithTitle(""):
        title = window.title.lower()
        
        if any(browser in title for browser in ["chrome", "firefox", "edge", "opera", "brave"]):
            for word in BLOCKED_WORDS:
                if word in title:
                    print(f"🚨 Detected: '{word}' in the title '{title}'. Closing browser...")

                    # Terminate browser processes
                    for pid in browser_windows:
                        try:
                            psutil.Process(pid).kill()  # `kill()` is more aggressive than `terminate()`
                        except (psutil.NoSuchProcess, psutil.AccessDenied):
                            pass  # Process might already be closed
                    time.sleep(2)
                    return  # Exit after closing the browser

# Run continuously
while True:
    close_browser()

    # Relaunch blocker if it was stopped
    if not is_process_running("blocker.exe"):  
        subprocess.Popen(["C:\\Users\\Kusal Darshana\\Documents\\dist\\blocker.exe"], shell=True)

    time.sleep(5)  # Check every 5 seconds
