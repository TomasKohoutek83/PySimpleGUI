import PySimpleGUI as sg
import csv
import os

layout = [
    [sg.Text('Chosse a CSV file:')],
    [sg.InputText(key = '-FILE_PATH-'),
    sg.FileBrowse(initial_folder = working_directory)]
        ]





