import wolframalpha
client = wolframalpha.Client("Personal Client Key")

import wikipedia

import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) #changes voices. 1 for female
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 120)

import ssl

ssl._create_default_https_context = ssl._create_unverified_context

import PySimpleGUI as sg

sg.theme('LightTeal')

layout = [  [sg.Text("Hey beautiful, I'm August. How can I help you today?")],
            [sg.Text('What do you need help with?'), sg.InputText()],
            [sg.Button('Search'), sg.Button('Cancel')] ]

window = sg.Window('August (PythonVirtualAssistant)', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    try:
        wiki_res = wikipedia.summary(values[0], sentences=3)
        wolf_res = next(client.query(values[0]).results).text
        engine.say(wolf_res)
        sg.PopupNonBlocking("WolframAlpha Findings: \n" + wolf_res, "Wikipedia Page: \n" + wiki_res)
    except wikipedia.exceptions.DisambiguationError:
        wolf_res = next(client.query(values[0]).results).text
        engine.say(wolf_res)
        sg.PopupNonBlocking(wolf_res)
    except wikipedia.exceptions.PageError:
        wolf_res = next(client.query(values[0]).results).text
        engine.say(wolf_res)
        sg.PopupNonBlocking(wolf_res)
    except:
        wiki_res = wikipedia.summary(values[0], sentences=3)
        engine.say(wiki_res)
        sg.PopupNonBlocking(wiki_res)

    engine.runAndWait()

    print(values[0])


window.close()
