import PySimpleGUI as sg
import threading
from time import sleep
import pyautogui
from random import randint

sg.theme('Dark Grey 13')

layout_hotkey = [
  [sg.Push(), sg.Text('Hotkey'), sg.Push()],
  [sg.Text('Hotkey 1'), sg.Input(key='-HOTKEY_1-', s=10, default_text='A')],
]

layout_time = [
  [sg.Push(), sg.Text('Hotkey deley '), sg.Push()],
  [sg.Text('Time'), sg.Input(key='-HOTKEY_TIME_1-',s=10, default_text=5)],
]

layout_time_start = [
  [sg.Push(), sg.Text('Start deley'), sg.Push()],
  [sg.Input(key='-TIME_START-', s=10, default_text=5)],
]

layout = [
  [sg.StatusBar('StatusBar', s=10), sg.StatusBar('Threds: ',)],
  [sg.Output(size=(70,12))],
  [sg.Column(layout_hotkey), sg.VSeparator(), sg.Column(layout_time), sg.VSeparator(), sg.Column(layout_time_start)],
  [sg.Button('Start', p=10), sg.Button('Stop')]
]

window = sg.Window(
  'Macro',
  layout = layout,
  element_justification='c',
)

global starter 
starter = False

def operation_thread(seconds, window):
  print('Starting thread - will sleep for {} seconds'.format(deley_start))
  sleep(deley_start)
  print('Go!')
  count = 0
  while starter:
    if starter == False:
      break
    sleep(seconds)   
    count += 1
    print('Hotkey: ', hotkey, ' -- Deley: ', seconds_hotkey, '-- Count: ', count)
    press_hotkey()

  print('-THREAD-', '** DONE **')

def press_hotkey():
  if len(hotkey) >= 2:
    pyautogui.hotkey(hotkey[0], hotkey[1])
  else: pyautogui.hotkey(hotkey[0])

while True:
  event, values = window.read()
  #print(event, values) 
      
  string_hotkey = values["-HOTKEY_1-"]
  hotkey = string_hotkey.split(' ')
  seconds_hotkey = int(values["-HOTKEY_TIME_1-"])   
  deley_start = int(values["-TIME_START-"])

  if event == 'Start':
    starter = True
  else: starter = False

  if event in (sg.WIN_CLOSED, 'Exit'):
    break
  elif event.startswith('Start'):
    print('Thread alive! value: {}'.format(seconds_hotkey))
    threading.Thread(target=operation_thread, args=(seconds_hotkey, window), daemon=True).start()
