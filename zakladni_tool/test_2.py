# Crating a form and using radio button
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
        pg.Radio("Python","group 1"),
        pg.Radio("Java", 'group 2')
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

    if event == pg.WIN_CLOSED or event == "Close" :
         break
    elif event ==  "Ok":
        print(f"Name: {values[0]}")
        print(f"Age: {values[1]}")
        print(f"Email: {values[2]}")
        language = "Java"
        if values[3] == True:
            language = "Python"
        print(f"Favourite language: {language}")
        for item in values:
            values[item] = None


#Close Window
window.close()
exit()


