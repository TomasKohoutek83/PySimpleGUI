import PySimpleGUI as pg

# Setup theme
pg.theme("DarkAmber")

# Create layout
layout = [
    [pg.Text("Enter name")],
    [pg.Input()],
    [pg.Button("ok"),pg.Button("Cancel")]
]

# Create window
window  =pg.Window("Form", layout)

# Event loop
while True:
    event, values = window.read()
    if event == "Cancel" or event == pg.WIN_CLOSED:
        break
    print(values[0])

#Close window
window.close()