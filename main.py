# you need to install PySimpleGUI Before you can run 
import PySimpleGUI as sg   #importing the main lib and namming it as sg
layout = [[sg.Input(key='-input-',enable_events=True),sg.Spin(['KG-->G','M-->CM','GB-->MB','MG-->KB'],enable_events=True,key='-spn-')],
          [sg.Text('    kareem      ',key='txt',enable_events=True),sg.Button('Convert',key='-btn-')]]

window = sg.Window('Converter',layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED :
        break
    input_values = values['-input-']
    if event == '-btn-':
        if input_values.isnumeric() :
            # match values['-spn-'] :
            #     case 'KG-->G' :
            #        window['txt'].update(values['-input-']+' KeloGrams = '+str(int(values['-input-'])*1000)+' Grams')
            #     case 'M-->CM' :
            #         window['txt'].update(values['-input-']+' Meter = '+str(int(values['-input-'])*1000)+' Centimeter')
            #     case 'GB-->MB':
            #         window['txt'].update(values['-input-']+' Gigabytes = '+str(int(values['-input-'])*1024)+' Megabytes')
            #     case 'MG-->KB' :
            #         window['txt'].update(values['-input-']+' Megabytes = '+str(int(values['-input-'])*1024)+' Kelobytes')
            if values['-spn-'] == 'KG-->G':
               window['txt'].update(values['-input-']+' KeloGrams = '+str(int(values['-input-'])*1000)+' Grams')
            elif values['-spn-'] == 'M-->CM':
               window['txt'].update(values['-input-']+' Meter = '+str(int(values['-input-'])*1000)+' Centimeter')
            elif values['-spn-'] == 'GB-->MB':
               window['txt'].update(values['-input-']+' Gigabytes = '+str(int(values['-input-'])*1024)+' Megabytes')
            elif values['-spn-'] == 'MG-->KB':
               window['txt'].update(values['-input-']+' Megabytes = '+str(int(values['-input-'])*1024)+' Kelobytes')
window.close()
