import PySimpleGUI as sg
import Script as Macro

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

  HOTEY_1 = Macro
  if START:
    HOTEY_1.Macro.__init__
    (values["-TIME_START-"],
     values["-HOTKEY_1-"], 
     values["-HOTKEY_TIME_1-"],
     values["-TIME_STOP-"])

    print(values["-TIME_START-"])

    HOTEY_1.Macro.event(HOTEY_1, START)

  
  print(HOTEY_1.Macro.rand_time(20))

  if values == None or event == sg.WIN_CLOSED:
    break