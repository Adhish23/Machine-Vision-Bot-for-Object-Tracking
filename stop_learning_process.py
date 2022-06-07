import keyboard
import glob
import subprocess
import re
import os
import array as arr
import time

 #Stop the Training process started after pressing previous button 
keyboard.press_and_release('ctrl + c')
time.sleep(5)
##keyboard.press_and_release('ctrl + c')
##keyboard.press_and_release('ctrl + c')
keyboard.press_and_release('ctrl + y')
time.sleep(2)
keyboard.press_and_release('Enter')
time.sleep(5)
##keyboard.press_and_release('ctrl + c')
#sleep(1)
os.system(r"python C:/Users/Admin/Desktop/KJSCE_Object_Detection/api.py")
