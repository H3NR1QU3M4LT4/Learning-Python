import sys
import subprocess
import time
import pyautogui
import pandas as pd
from datetime import datetime

zoom = 'C:\\Users\\Henrique Malta\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe'
linksbct = 'https://videoconf-colibri.zoom.us/j/84503647996?pwd=dENoYlNTRGtubDJMaTltemRzWWhxdz09#success'
def sign_in (link):
    subprocess.call(zoom)

sign_in(linksbct)