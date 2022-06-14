from ast import Break
from PySimpleGUI import (Window, Button, Text, Image, Input, Column, VSeparator, Push, theme, popup)

theme('darkPurple2')

layout_direita = [
  [Text('E-mail'), Input(key='-EMAIL-')],
  [Text('Senha'), Input(password_char='*', key='-SENHA-')],
  [Push(), Button('Login'), Push(), Button('Esqueci a Senha'), Push()]
]

layout_esquerda = [
  [Image(filename='Human.png', key='-IMAGE-')]
]

layout = [
  [Image(filename='simpe.jpg')],
  [Column(layout_esquerda), VSeparator(), Column(layout_direita)]
]

window = Window(
  'Macro Ninfox',
  layout = layout,
  #element_justification='c'
)

while True:
  event, values = window.read()
  print(event,' - ', values)

  def interface(value):
    if value == 'Login':
      print('Butao de login')
    if value == 'Esqueci a Senha':
      popup(f'Seu email é {values["-EMAIL-"]}')

  interface(event)
  
  if values == None:
    break  

  
