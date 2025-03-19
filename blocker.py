import time
import psutil
import pygetwindow as gw
# from plyer import notification

# Add your blocked words here
BLOCKED_WORDS = ["porn", "18+", "orgasm", "eporner", "pornhub", "xhasmster", "xvideo", "pornstar", "cum", "masturbate", "missax", "sex", "leaked","wal", "wal katha", "walkatha", "wala", "nude","naked", "jerk off", "වල්කතා", "වැල", "වල් කතා", "හුකන", "පුකේ", "හුත්ත", "වේසි", "හුකනවා", "හැමිනෙනවා", "hardcore", "erotic", "hentai", "bdsm", "taboo", "shemale", "camgirl", "camsex", "escort", "milf", "deepthroat",  "blowjob", "handjob", "anal", "lesbian", "gay", "orgy", "threesome", "creampie", "dildo", "webcam sex", "onlyfans", "nsfw", "softcore", "futa", "boobs", "tits", "ass", "pussy", "dick", "cock", "squirting", "fingering", "pegging", "dominatrix", "mistress", "submissive", "kinky",  "cumshot",  "cuckold",  "stepmom", "gay porn", "webcam girl",  "stripper",  "busty", ]

# Function to check open browser windows
def get_browser_windows():
    browsers = ["chrome", "firefox", "edge", "opera", "brave"]
    browser_windows = []
    
    for proc in psutil.process_iter(['pid', 'name']):
        for browser in browsers:
            if browser in proc.info['name'].lower():
                browser_windows.append(proc.info['pid'])
    return browser_windows

# Function to close browser if bad word is found
def close_browser():
    # Get all open windows and filter only browsers
    browser_windows = get_browser_windows()
    for window in gw.getWindowsWithTitle(""):
        title = window.title.lower()
        
        # Check if the window belongs to a browser and if it contains blocked words
        if any(browser in title for browser in ["chrome", "firefox", "edge", "opera", "brave"]):
            for word in BLOCKED_WORDS:
                if word in title:
                    # # Print and show notification with blocked word
                    # print(f"🚨 Detected: '{word}' in the title '{title}'. Closing browser...")
                    # notification.notify(
                    #     title='Blocked Content Detected',
                    #     message=f"Browser closed due to detected word: {word}",
                    #     timeout=10  # Notification duration in seconds
                    # )
                    for pid in browser_windows:
                        try:
                            psutil.Process(pid).terminate()
                        except psutil.NoSuchProcess:
                            pass
                    time.sleep(2)
                    break  # Exit the loop after finding the first matching word

# Run continuously
while True:
    close_browser()
    time.sleep(5)  # Check every 5 seconds
