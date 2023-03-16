# you need to install PySimpleGUI Before you can run 
import PySimpleGUI as sg   #importing the main lib and namming it as sg
layout = [[sg.Input(key='-input-',enable_events=True),sg.Spin(['KG-->G','M-->CM','GB-->MB','MG-->KB'],enable_events=True,key='-spn-')],
          [sg.Text('    kareem      ',key='txt',enable_events=True),sg.Button('Convert',key='-btn-')]]

window = sg.Window('Converter',layout)
while True:
    event, value = window.read()
    if event == sg.WIN_CLOSED :
        break
    if event == '-btn-' and value['-spn-'] == 'KG-->G':
        window['txt'].update(value['-input-']+' KeloGrams = '+str(int(value['-input-'])*1000)+' Grams')
    elif event == '-btn-' and value['-spn-'] == 'M-->CM':
        window['txt'].update(value['-input-']+' Meter = '+str(int(value['-input-'])*1000)+' Centimeter')
    elif event == '-btn-' and value['-spn-'] == 'GB-->MB':
        window['txt'].update(value['-input-']+' Gigabytes = '+str(int(value['-input-'])*1024)+' Megabytes')
    elif event == '-btn-' and value['-spn-'] == 'MG-->KB':
        window['txt'].update(value['-input-']+' Megabytes = '+str(int(value['-input-'])*1024)+' Kelobytes')
window.close()
