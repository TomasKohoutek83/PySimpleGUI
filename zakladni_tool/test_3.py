
# Check box,comboboxes,listboxes,sliders
import PySimpleGUI as pg

#Setup theme
pg.theme("BlueMono")

#Create layout
layout= [
    [
        pg.Text("Enter name: ", size= (10,1)),
        pg.InputText(do_not_clear= False)
    ],
    [
        pg.Text("Enter age: ",size= (10,1)),
        pg.InputText(do_not_clear= False)

    ],
    [
        pg.Text("Enter email: ",size= (10,1)),
        pg.InputText(do_not_clear= False)
    ],
    [
        pg.Text("Favorite languge:"),
        #Rozeviraci seznam
        #pg.Combo(["Python","Java","C","C++","JavaScript"])
        # Rolovaci seznam + Multiple - vice moznosti na vyber
        pg.Listbox(["Python","Java","C","C++","JavaScript"], size = (30,4), select_mode = pg.LISTBOX_SELECT_MODE_MULTIPLE)

    ],
    [
        # posuvny ukazatel
        pg.Text("Experience (years):"),
        pg.Slider(range=(1,10), default_value=3 ,size =(20,15),orientation="horizontal")

    ],
    [
        pg.Button("Ok"),
        pg.Button("Close")
    ]
        ]

#Create window
window = pg.Window("Info", layout)
#Event loop
while True:
    event, values = window.read()
    # Tisk hodnot pro kotrolun umisteni hodnoty
    print(values)
    if event == pg.WIN_CLOSED or event == "Close" :
         break
    elif event ==  "Ok":
        print(f"Name: {values[0]}")
        print(f"Age: {values[1]}")
        print(f"Email: {values[2]}")
        print(f"favourite language: {values[3]}")
        print(f"Experience (years): {values[4]}")

        for item in values:
            values[item] = None


#Close Window
window.close()
exit()
