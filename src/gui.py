#Importación de librerías
import PySimpleGUI as sg


file_column = [
    [sg.Text("Elige juego: ", font= (13))],
    [sg.Button("Ahorcado", key="HANG",size=(0,1), font=(3)), 
    sg.T('', size=(24,4)), 
    sg.Button("Buscaminas", key="MINE",size=(0,1), font=(3)),
    sg.T('', size=(24,4)), 
    sg.Button("Agenda", key="SCHED",size=(0,1), font=(3))],
    [sg.HorizontalSeparator()],
]


layout = [
    [sg.Column(file_column)]
]

window = sg.Window(title ="MiX-MiniGames", layout = layout, size=(900,500), margins=(100, 50))

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

