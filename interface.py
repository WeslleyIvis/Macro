from PySimpleGUI import (Window, Button, Text, Image, Input, Column, VSeparator)

layout_direita = [
  [Text('E-mail'), Input()],
  [Text('Senha'), Input(password_char='*')],
  [Button('Login'), Button('Esqueci a Senha')]
]

layout_esquerda = [
  [Image(filename='Human.png')]
]

layout = [
  [Column(layout_esquerda), VSeparator(), Column(layout_direita)]
]

window = Window(
  'Macro Ninfox',
  layout = layout,
  #element_justification='c'
)

print(window.read())

window.close()