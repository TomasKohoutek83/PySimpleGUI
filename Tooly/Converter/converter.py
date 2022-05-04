import PySimpleGUI as sg

layout=[
    [sg.Text('Text', enable_events = True, key = '-TEXT-'), sg.Spin(['Item 1', 'Item 2'])],
    [sg.Button('Button', key = '-BUTTON1-')],
    [sg.Input(key = '-INPUT-')],
    [sg.Text('Test'), sg.Button('Button', key = '-BUTTON2-')]
        ]

window = sg.Window('Converter', layout)

while True:
    event, values = window.read()

    if event == sg. WIN_CLOSED:
        break

    if event =='-BUTTON1-':
        window['-TEXT-'].update(values['-INPUT-'])

    if event == '-BUTTON2-':
        print("something")

    if event == '-TEXT-':
        print('text was pressed')


window.close()