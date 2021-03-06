import PySimpleGUI as sg
import csv
import os

working_directory = os.getcwd()

layout = [
    [sg.Text('Chosse a CSV file:')],
    [sg.InputText(key = '-FILE_PATH-'),
    sg.FileBrowse(initial_folder = working_directory, file_types=[('CSV Files','*csv')])],
    [sg.Button('Submit'), sg.Exit()]

        ]


window = sg.Window("Browser", layout)

def display_csv_array(csv_address):
    file = open(csv_address)
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    rows = []
    for row in csv_reader:
        rows.append(row)
    file.close()
    return rows

while True:
    event,values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    elif event == 'Submit':
        csv_address = values['-FILE_PATH-']
        print(display_csv_array(csv_address))

window.close()




