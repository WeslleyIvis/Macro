import pyautogui
from time import sleep

sleep(2)
currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX, currentMouseY)

sleep(1)
pyautogui.moveTo(10/100 * currentMouseX + currentMouseX, currentMouseY)
sleep(1)
pyautogui.moveTo(10/100 * currentMouseX + currentMouseX, currentMouseY - 15/100 * currentMouseY)
sleep(1)
pyautogui.moveTo(currentMouseX, currentMouseY - 15/100 * currentMouseY)
sleep(1)
pyautogui.moveTo(currentMouseX - 7/100 * currentMouseX, currentMouseY - 15/100 * currentMouseY)
sleep(1)
pyautogui.moveTo(currentMouseX - 7/100 * currentMouseX, currentMouseY)
sleep(1)
pyautogui.moveTo(currentMouseX - 7/100 * currentMouseX, currentMouseY + 15/100 * currentMouseY) 
sleep(1)
pyautogui.moveTo(currentMouseX, currentMouseY + 15/100 * currentMouseY) 
sleep(1)
pyautogui.moveTo(currentMouseX + 7/100 * currentMouseX, currentMouseY + 15/100 * currentMouseY) 


screenWidth, screenHeight = pyautogui.size()
# print(screenWidth, screenHeight)
# print(50/100 * screenWidth, 50/100 * screenHeight)
#pyautogui.click()
