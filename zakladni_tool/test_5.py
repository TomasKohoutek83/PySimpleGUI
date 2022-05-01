# Updating windows after event

import os
import PySimpleGUI as pg

pg.theme("DarkBlue")

file_list_column =[
    [
        pg.Text("Folder"),
        pg.In(size = (30,1), enable_events =True, key = "-FOLDER-"),
        pg.FolderBrowse(),
    ],
    [
        pg.Listbox(
            values = [],
            enable_events= True,
            size=(50,20),
            key = "-FILE_LIST-"
                )
    ]
]

file_viewer_column = [
    [pg.Text("Choose a file from the list", size = (50,1))],
    [pg.Text("File name: ", size=(70,3), key = "-TOUT-")],
    [pg.Multiline(size=(70,30), key= "-TEXT-")],
    [pg.Button("Save")]
                    ]
layout = [
    [
        pg.Column(file_list_column),
        pg.VSeparator(),
        pg.Column(file_viewer_column)
    ]
]

window = pg.Window("FIle viewer", layout)

folder_location = ""


while True:
    event, values = window.read()
    if event== pg.WIN_CLOSED or event == "Exit":
        break
    elif event == "-FOLDER-":
        folder_location  = values["-FOLDER-"]
        try:
            files = os.listdir(folder_location)

        except:
            files = []

        file_names = [
            file for file in files
            if os.path.isfile(os.path.join(folder_location, file))
            and file.lower().endswith((".txt", ".csv", ".json", ".py"))
        ]
        window["-FILE_LIST-"].update(file_names)

    elif event == "-FILE_LIST-" and len(values["-FILE_LIST-"]) >0 :
        file_selection = values["-FILE_LIST-"][0]
        with open(os.path.join(folder_location, file_selection)) as file:
            contents = file.read()
            window["-TOUT-"].update(os.path.join(folder_location, file_selection))
            window["-TEXT-"].update(contents)

    elif event == "Save" and len(values["-FILE_LIST-"]) > 0:
        file_selection = values["-FILE_LIST-"][0]
        with open(os.path.join(folder_location, file_selection), 'w') as file:
            file.write(values["-TEXT-"])


window.close()
exit()

