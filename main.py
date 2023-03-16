import PySimpleGUI as sg   #importing the main lib and namming it as sg
layout = [
    [sg.Text('Text',enable_events=True,key='-txt-'),sg.Spin('item_1','item_2','item_3')],
    [sg.Button('Button',key='-button1-')],
    [sg.Input('hee',enable_events=True,key="-inp-")],
    ]    # splitting the window to three columns and putting wideget or element in avery one of it
window = sg.Window('Converter',layout)
conter = 0
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    