import os, time
import subprocess
from collections import Counter

wait_seconds = 3600

while True:
    try:
        p = subprocess.Popen('Cry.ConsoleApp.exe', creationflags=subprocess.CREATE_NEW_CONSOLE)
        time.sleep(wait_seconds)
        p.terminate()
    except Exception as e: print(e)
