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

'''screenWidth, screenHeight = pyautogui.size()
pyautogui.moveTo(screenWidth / 2, screenHeight / 2)
currentMouseX, currentMouseY = pyautogui.position()
pyautogui.moveTo(100, 150)
pyautogui.click()
pyautogui.moveRel(None, 10)  # move mouse 10 pixels down
pyautogui.doubleClick()
pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)  # use tweening/easing function to move mouse over 2 seconds.
pyautogui.typewrite('Hello world!', interval=0.25)  # type with quarter-second pause in between each key
pyautogui.press('esc')
pyautogui.keyDown('shift')
pyautogui.press(['left', 'left', 'left', 'left', 'left', 'left'])
pyautogui.keyUp('shift')

distance = 200
while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.5)   # move right
    distance -= 5
    pyautogui.dragRel(0, distance, duration=0.5)   # move down
    pyautogui.dragRel(-distance, 0, duration=0.5)  # move left
    distance -= 5
    pyautogui.dragRel(0, -distance, duration=0.5)  # move up'''