from time import sleep
import pyautogui

contador = range(5)
ring = []
TIME = 5
TIMERING = 1200
soft_time = 0

def fazer_runa():
  pyautogui.press('7')
  pyautogui.press('8')
  

while True: 
  sleep(TIME)
  fazer_runa()
  ring.append(TIME)
  if sum(ring) >= TIMERING:
    pyautogui.hotkey("ctrl", "2") 
    ring.clear()

