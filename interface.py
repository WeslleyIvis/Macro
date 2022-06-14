import PySimpleGUI as sg
#import script as Macro
from time import sleep
from random import randint
import pyautogui

class Macro:
  def __init__(self,value_start,stop,hotkey,time_hotkey):
    self.value_start = int(value_start)
    self.stop = int(stop)
    self.hotkey = hotkey
    self.time_hotkey = time_hotkey
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

  def rand_time(self, value:int):
    value += randint(-10, 10)
    return value

  def init(self, true_false:bool):
    self.event(true_false)

sg.theme('darkPurple2')

layout_hotkey = [
  [sg.Push(), sg.Text('HOTKEYS'), sg.Push()],
  [sg.Text('Hotkey 1'), sg.Input(key='-HOTKEY_1-', s=10)],
  [sg.Text('Hotkey 2'), sg.Input(key='-HOTKEY_2-', s=10)],
  [sg.Text('Hotkey 3'), sg.Input(key='-HOTKEY_3-', s=10)],
]

layout_time = [
  [sg.Push(), sg.Text('TIME ACTIONS'), sg.Push()],
  [sg.Text('Time'), sg.Input(key='-HOTKEY_TIME_1-',s=10)],
  [sg.Text('Time'), sg.Input(key='-HOTKEY_TIME_2-',s=10)],
  [sg.Text('Time'), sg.Input(key='-HOTKEY_TIME_3-',s=10)],
]

layout_time_start = [
  [sg.Push(), sg.Text('START IN'), sg.Push()],
  [sg.Input(key='-TIME_START-', s=10)],
  [sg.Push(), sg.Text('STOP IN'), sg.Push()],
  [sg.Input(key='-TIME_STOP-', s=10)]
]

layout = [
  [sg.Column(layout_hotkey), sg.VSeparator(), sg.Column(layout_time), sg.VSeparator(), sg.Column(layout_time_start)],
  [sg.Button('Start', p=10), sg.Button('Stop')]
]

window = sg.Window(
  'Macro',
  layout = layout,
  element_justification='c',
)

START = False

while True:
  event, values = window.read()
  print(event, values) 

  if event == 'Start':
    START = True
  else: START = False

  #HOTEY_1 = Macro()
  
  if START:
    HOTEY_1 = Macro(value_start = values["-TIME_START-"],
     stop = values["-HOTKEY_1-"], 
     hotkey = values["-HOTKEY_TIME_1-"],
     time_hotkey = int(values["-TIME_STOP-"])
    )
    

    print(values["-TIME_START-"])

    HOTEY_1.event(START)

  
  print(HOTEY_1.rand_time(20))

  if values == None or event == sg.WIN_CLOSED:
    break