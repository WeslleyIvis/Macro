import PySimpleGUI as sg
import threading
from time import sleep
import pyautogui
from random import randint

sg.theme('Dark Grey 13')

layout_hotkey = [
	
	[sg.Push(), sg.Text('Hotkey'), sg.Push()],
	[sg.Text('Hotkey 1'), sg.Input(key='-HOTKEY_0-',
	s=10, 
	default_text='7')],
	[sg.Text('Hotkey 2'), sg.Input(key='-HOTKEY_1-',
	s=10, 
	default_text='8')],
	[sg.Text('Hotkey 3'), sg.Input(key='-HOTKEY_2-',
	s=10, 
	default_text='Ctrl 2')],
		[sg.Text('Hotkey 4'), sg.Input(key='-HOTKEY_3-',
	s=10, 
	default_text='9')],
]

layout_time = [
	[sg.Push(), sg.Text('Hotkey deley '), sg.Push()],
	[sg.Text('Time'), sg.Input(key='-HOTKEY_TIME_0-',
		s=10, 
		default_text=60,
		enable_events=True)],
	[sg.Text('Time'), sg.Input(key='-HOTKEY_TIME_1-',
		s=10, 
		default_text=300,
		enable_events=True)],
	[sg.Text('Time'), sg.Input(key='-HOTKEY_TIME_2-',
		s=10, 
		default_text=1200,
		enable_events=True)],
	[sg.Text('Time'), sg.Input(key='-HOTKEY_TIME_3-',
		s=10, 
		default_text=1200,
		enable_events=True)],
]

layout_time_start = [
	[sg.Push(), sg.Text('Start deley'), sg.Push()],
	[sg.Input(key='-TIME_START-',
		s=10,
		default_text=1, )],
]

layout_macro_loot = [
	[sg.Push(), sg.Text('Window'), sg.Push()],
	[sg.Input(key='')]
]

layout = [
	[sg.StatusBar(text='StatusBar: ', text_color='Green',  s=10, key='-STATUS-'), sg.StatusBar('Threads: ', key='-ON-THREADS-')],
	[sg.Output(size=(70,12))],
	[sg.Column(layout_hotkey), sg.VSeparator(), sg.Column(layout_time), sg.VSeparator(), sg.Column(layout_time_start)],
	[sg.Button('Start', p=10, s=10), sg.Button('Stop', s=10)],
	[sg.HSeparator()],
	[layout_macro_loot]
]

window = sg.Window(
	'Macro',
	layout = layout,
	element_justification='c',
)

global starter 
starter = False

def operation_thread(seconds, hotkey, window):
	print('Starting thread - will sleep for {} seconds \n'.format(deley_start))
	count = 0
	sleep(deley_start)

	print('Go!')
	while starter:
		if starter == False:
			break
		sleep(seconds)   
		count += 1
		print('Hotkey: ', hotkey, ' -- Deley: ', seconds, '-- Count: ', count)
		press_hotkey(hotkey)
		#seconds = vary_time(seconds, -5, 5)
	print('-THREAD-', '** DONE ** \n')

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

def vary_time(seconds, min, max):
	seconds += randint(min, max)
	return seconds

while True:
	event, values = window.read()	
	#print(event, values) 
    
	if event in (sg.WIN_CLOSED, 'Exit'):
		break

	seconds_hotkey = {
		'value_0': valid_value(values["-HOTKEY_TIME_0-"]),
		'value_1': valid_value(values["-HOTKEY_TIME_1-"]),
		'value_2': valid_value(values["-HOTKEY_TIME_2-"]),
		'value_3': valid_value(values["-HOTKEY_TIME_3-"]),
	}

	for x in range(len(seconds_hotkey)):
		if event == f'-HOTKEY_TIME_{x}-' and values[f'-HOTKEY_TIME_{x}-'] and values[f'-HOTKEY_TIME_{x}-'][-1] not in ('0123456789.-'):
			window[f'-HOTKEY_TIME_{x}-'].update(values[f'-HOTKEY_TIME_{x}-'][:-1])

	hotkey = {
		'hotkey_0': values["-HOTKEY_0-"].split(' '),
		'hotkey_1': values["-HOTKEY_1-"].split(' '),
		'hotkey_2': values["-HOTKEY_2-"].split(' '),
		'hotkey_3': values["-HOTKEY_3-"].split(' '),
	}
	deley_start = valid_value(values["-TIME_START-"])

	for x in seconds_hotkey:
		if event == 'Start' and type(seconds_hotkey[x]) == int and type(deley_start) == int:
				starter = True

	if event.startswith('Start') and starter == True:		
		for x in range(len(hotkey)):
			if seconds_hotkey[f'value_{x}'] < 1:
				print(f'-HOTKEY- : -- {x} -- : ',hotkey[f'hotkey_{x}'], '** OFF ** \n')
			else:
				print('Thread alive! value: {}'.format(seconds_hotkey[f'value_{x}']))
				threading.Thread(target=operation_thread, args=(seconds_hotkey[f'value_{x}'], hotkey[f'hotkey_{x}'], window), daemon=True).start()
		

