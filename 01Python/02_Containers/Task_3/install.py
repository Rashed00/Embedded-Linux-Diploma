#!/usr/bin/python3

import pyautogui

pyautogui.click(88,303)
pyautogui.countdown(1)
pyautogui.tripleClick(327,142)
pyautogui.countdown(1)
pyautogui.press('backspace')
pyautogui.countdown(1)
pyautogui.write("C++ TestMate",interval=0.25)
pyautogui.countdown(3)
extensionPosition = pyautogui.locateOnScreen("cpptestmate.png")



if extensionPosition == None:
    print("Extension not found!\nClosing app...")
else:
    print("Check.")
    pyautogui.click(extensionPosition.top,extensionPosition.left)
    pyautogui.countdown(1)
    uninsatllPosition = pyautogui.locateOnScreen("uninstall.png")
    if uninsatllPosition == None:
        pyautogui.click(664,250)
        print("Installing extension...")
    else:
        print("Extension is already insatlled.")
