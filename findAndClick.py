import time
import pyautogui

def findAndClick(delay,target):
    time.sleep (delay)
    #print(pyautogui.locateCenterOnScreen(target))
    pyautogui.click(pyautogui.locateCenterOnScreen(target))