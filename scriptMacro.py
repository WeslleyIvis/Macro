from pickle import FALSE
from time import sleep
from random import randint
import pyautogui

class Macro:
  def __init__(self, hotkey):
    self.hotkey_1 = hotkey_1


value = True

hotkey_1 = ['ctrl', '2']
count_hotkey_1 = []
TIME_HOTKEY_1 = 1200

hotkey_2 = ['8']
count_hotkey_2 = []
TIME_HOTKEY_2 = 180

hotkey_3 = ['7']

TIME = [60, -10, 10]
START = 5

hotkey_soft = []
count_soft = []
TIMESOFT = 0

def rand_time(value, min, max):
  value += randint(min, max)
  return value

def use_food(time, hotkey):
  if time >= TIME_HOTKEY_2:
    pyautogui.press(hotkey)
    count_hotkey_2.clear()

def fazer_runa(hotkey):
  pyautogui.press(hotkey)
  
def life_ring(time):
  if time >= TIME_HOTKEY_1:
    if len(hotkey_1) == 2:
      pyautogui.hotkey(hotkey_1[0], hotkey_1[1])
    else:
      pyautogui.hotkey(hotkey_1[0])
    count_hotkey_1.clear()
    return

def count_alltime(time):
  count_hotkey_1.append(time)
  count_hotkey_2.append(time)
  count_soft.append(time)

while value:  
  print(START)
  sleep(START)
  START = rand_time(TIME[0], TIME[1], TIME[2])
  count_alltime(START)
  fazer_runa(hotkey_3[0])
  use_food(sum(count_hotkey_2), hotkey_2)
  life_ring(sum(count_hotkey_1))
