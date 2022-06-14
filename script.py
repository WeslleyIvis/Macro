from time import sleep
from random import randint
import pyautogui

class Macro:
  def __init__(self):
    self.value_start = 5
    self.stop = 20
    self.hotkey = '1'
    self.time_hotkey = 10
    self.COUNT_TIME = []
    self.COUNT_STOP = []

  def event(self, value:bool):
    while value:
      #print('start')
      sleep(self.value_start)
      self.value_start = self.rand_time(self.time_hotkey)
      self.append_time()
      self.start_hotkey()

      if sum(self.COUNT_STOP) >= self.stop:
        break

  def append_time(self):
    self.COUNT_TIME.append(self.value_start)
    self.COUNT_STOP.append(self.value_start)

  def start_hotkey(self):
    if sum(self.COUNT_TIME) >= self.time_hotkey:
      pyautogui.hotkey(self.hotkey)
    self.COUNT_TIME.clear()

  def rand_time(self, value):
    value += randint(-10, 10)
    return value

  def init(self, true_false:bool):
    self.event(true_false)

#teste = Macro()
#print(teste.init(True), 'teste')
