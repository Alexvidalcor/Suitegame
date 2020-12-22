#Importación de librerías
import PySimpleGUI as sg

def MainGui():
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

    window = sg.Window(title ="Suite-MiniGames", layout = layout, size=(900,500), margins=(100, 50))
    while True:
        event, values = window.read()
        if event == "HANG":
            exec(open("src/ProgMain/HangMain.py").read())
        if event == "MINE":
            exec(open("src/ProgMain/MineMain.py").read())
        if event == "SCHED":
            exec(open("src/ProgMain/SchedMain.py").read())
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
    window.Close()

