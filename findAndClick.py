import time
import pyautogui

def findAndClick(delay,target):
    time.sleep (delay)
    #print(pyautogui.locateCenterOnScreen(target))
    pyautogui.click(pyautogui.locateCenterOnScreen(target))

def findTarget(delay,target):
    time.sleep (delay)
    #print(pyautogui.locateCenterOnScreen(target))
    return (pyautogui.locateCenterOnScreen(target))

def findAndSelect(delay,target):
    time.sleep (delay)
    #print(pyautogui.locateCenterOnScreen(target))
    pyautogui.moveTo(pyautogui.locateCenterOnScreen(target))
    pyautogui.click()
    time.sleep (delay)
    pyautogui.press('space')