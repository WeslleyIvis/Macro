import PySimpleGUI as sg
import threading
from time import sleep
import pyautogui
from random import randint

sg.theme('Dark Grey 13')

layout_hotkey = [
  [sg.Push(), sg.Text('Hotkey'), sg.Push()],
  [sg.Text('Hotkey 1'), sg.Input(key='-HOTKEY_1-',
      s=10, 
      default_text='A')],
  [sg.Text('Hotkey 2'), sg.Input(key='-HOTKEY_2-',
      s=10, 
      default_text='7')],
  [sg.Text('Hotkey 3'), sg.Input(key='-HOTKEY_3-',
      s=10, 
      default_text='Ctrl 2')],
  [sg.Text('Hotkey 4'), sg.Input(key='-HOTKEY_4-',
      s=10, 
      default_text='9')],
]

layout_time = [
  [sg.Push(), sg.Text('Hotkey deley '), sg.Push()],
  [sg.Text('Time'), sg.Input(key='-HOTKEY_TIME_1-',
     s=10, 
     default_text=5)],
  [sg.Text('Time'), sg.Input(key='-HOTKEY_TIME_2-',
     s=10, 
     default_text=5)],
  [sg.Text('Time'), sg.Input(key='-HOTKEY_TIME_3-',
     s=10, 
     default_text=5)],
  [sg.Text('Time'), sg.Input(key='-HOTKEY_TIME_4-',
     s=10, 
     default_text=5)],
]

layout_time_start = [
  [sg.Push(), sg.Text('Start deley'), sg.Push()],
  [sg.Input(key='-TIME_START-',
   s=10,
   default_text=5)],
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

def operation_thread(seconds, hotkey, window):
  print('Starting thread - will sleep for {} seconds'.format(deley_start))
  count = 0
  sleep(deley_start)

  print('Go!')
  while starter:
    if starter == False:
      break
    elif seconds < 1:
      print(f'{hotkey}: OFF')
      break
    sleep(seconds)   
    count += 1
    print('Hotkey: ', hotkey, ' -- Deley: ', seconds, '-- Count: ', count)
    press_hotkey(hotkey)
  print('-THREAD-', '** DONE **')

def press_hotkey(hotkey_button):
  if len(hotkey_button) >= 2:
    pyautogui.hotkey(hotkey_button[0], hotkey_button[1])
  else: pyautogui.hotkey(hotkey_button[0])

def valid_value(value):
  if type(value) != int:
    if value.isnumeric():
      value = int(value)
    else: 
      sg.popup(f'Invalid value: {value}  -- APENAS NUMEROS--')
  return value

while True:
  event, values = window.read()
  print(event, values) 

  deley_start = valid_value(values["-TIME_START-"])
  seconds_hotkey = {
    'value_1': valid_value(values["-HOTKEY_TIME_1-"]),
    'value_2': valid_value(values["-HOTKEY_TIME_2-"]),
    'value_3': valid_value(values["-HOTKEY_TIME_3-"]),
    'value_4': valid_value(values["-HOTKEY_TIME_4-"])
    }
  hotkey = {
    'hotkey_1': values["-HOTKEY_1-"].split(' '),
    'hotkey_2': values["-HOTKEY_2-"].split(' '),
    'hotkey_3': values["-HOTKEY_3-"].split(' '),
    'hotkey_4': values["-HOTKEY_4-"].split(' '),
    }

  if event == 'Start' and type(seconds_hotkey['value_1']) == int and type(deley_start) == int:
    starter = True
  else:
     starter = False
     deley_start = 0
     seconds_hotkey = 0

  if event in (sg.WIN_CLOSED, 'Exit'):
    break
  elif event.startswith('Start') and starter == True:
    print('Thread alive! value: {}'.format(seconds_hotkey))
    threading.Thread(target=operation_thread, args=(seconds_hotkey['value_1'], hotkey['hotkey_1'], window), daemon=True).start()
    threading.Thread(target=operation_thread, args=(seconds_hotkey['value_2'], hotkey['hotkey_2'], window), daemon=True).start()
    threading.Thread(target=operation_thread, args=(seconds_hotkey['value_3'], hotkey['hotkey_3'], window), daemon=True).start()
    threading.Thread(target=operation_thread, args=(seconds_hotkey['value_4'], hotkey['hotkey_4'], window), daemon=True).start()
