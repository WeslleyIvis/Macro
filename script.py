from time import sleep
from random import randint
import pyautogui

contador = range(5)
count_ring = []
count_food = []
TIME = 1
TIMERING = 300
soft_time = 0

def rand_time(value, min, max):
  value += randint(min, max)
  return value

def use_food(time, hotkey):
  if time >= count_food:
    pyautogui.press(hotkey)

def fazer_runa(hotkey):
  pyautogui.press(hotkey)
  
def life_ring(time):
  if time >= TIMERING:
    pyautogui.hotkey("ctrl", "2")
    count_ring.clear()
    return

def count_alltime(time):
  count_ring.append(time)
  count_food.append(time)

while True:  
  sleep(TIME)
  TIME = rand_time(60, 0, 0)
  count_alltime(TIME)
  fazer_runa('7')
  use_food('8')
  life_ring(sum(count_ring))
