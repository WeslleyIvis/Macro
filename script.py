from time import sleep
from random import randint
import pyautogui

contador = range(5)

hotkey_ring = ['ctrl', '2']
count_ring = []
TIMERING = 1200

hotkey_food = ['8']
count_food = []
TIMEFOOD = 180

hotkey_runa = ['7']

TIME = [60, -10, 10]
START = 5

hotkey_soft = []
count_soft = []
TIMESOFT = 0

def rand_time(value, min, max):
  value += randint(min, max)
  return value

def use_food(time, hotkey):
  if time >= TIMEFOOD:
    pyautogui.press(hotkey)
    count_food.clear()

def fazer_runa(hotkey):
  pyautogui.press(hotkey)
  
def life_ring(time):
  if time >= TIMERING:
    if len(hotkey_ring) == 2:
      pyautogui.hotkey(hotkey_ring[0], hotkey_ring[1])
    else:
      pyautogui.hotkey(hotkey_ring[0])
    count_ring.clear()
    return

def count_alltime(time):
  count_ring.append(time)
  count_food.append(time)
  count_soft.append(time)

while True:  
  sleep(START)
  START = rand_time(TIME[0], TIME[1], TIME[2])
  count_alltime(START)
  fazer_runa(hotkey_runa[0])
  use_food(sum(count_food), hotkey_food)
  life_ring(sum(count_ring))
