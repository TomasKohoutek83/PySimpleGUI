import PySimpleGUI as sg




layout=[
    [
        sg.Input( key = '-INPUT-'),
        sg.Spin(['km to mile','kg to pound','sec to min'], key = '-UNITS-'),
        sg.Button('Convert', key = '-CONVERT-')
    ],
    [sg.Text('Output')]

]



window = sg.Window('Converter', layout)

while True:
    event, values = window.read()

    if event == sg. WIN_CLOSED:
        break

    if event == '-CONVERT-':
        input_value = values['-INPUT-']
        if input_value.isnumeric():
            match values['-UNITS-']:
                case 'km to mile':
                    output = float (input_value) * 0.6214
                    output_string = f'{input_value} km are {output} miles.'
            window['-OUTPUT-'].update(output_string)



window.close()