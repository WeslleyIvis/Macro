from time import sleep
from random import randint
import pyautogui

class Macro:
  def __init__(self, value_start = 5, hotkey = '1', time_hotkey = 5, stop = 20):
    self.START = value_start
    self.STOP = stop
    self.HOTKEY = hotkey
    self.TIME_HOTKEY = time_hotkey
    self.COUNT_TIME = []
    self.COUNT_STOP = []

  def event(self, value:bool):
    while value:
      #print('start')
      sleep(self.START)
      self.START = self.rand_time(self.TIME_HOTKEY)
      self.append_time()
      self.start_hotkey()

      if sum(self.COUNT_STOP) >= self.STOP:
        break

  def append_time(self):
    self.COUNT_TIME.append(self.START)
    self.COUNT_STOP.append(self.START)

  def start_hotkey(self):
    if sum(self.COUNT_TIME) >= self.TIME_HOTKEY:
      pyautogui.hotkey(self.HOTKEY)
    self.COUNT_TIME.clear()

  def rand_time(self, value):
    value += randint(-10, 10)
    return value

  def init(self, true_false:bool):
    self.event(true_false)

# teste = Macro()
# print(teste.init(True), 'teste')
