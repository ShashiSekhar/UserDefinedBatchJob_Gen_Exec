from pyautogui import *
import subprocess
import os
import time
def mvcl(a,b):
	moveTo(a,b)
	click()

print("Launching Firefox")
subprocess.Popen('firefox', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
time.sleep(2)
mvcl(650,117)
typewrite("moodlecc.vit.ac.in/login/index.php",interval=0.1)
press('enter')
time.sleep(2)
mvcl(680,415)
time.sleep(2)
mvcl(735,422)
typewrite("16BCE1286",interval=0.1)
press('tab')
press('enter')
mvcl(725,626)
scroll(-50)
