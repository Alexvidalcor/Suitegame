# Importación de librerías
import PySimpleGUI as sg
from subprocess import Popen, PIPE, STDOUT
import sys


def RunCommand(p, window=None):
    output=[]
    while True:
        output.append(p.stdout.read(1).decode())
        if output[-1].endswith('?'):
            print("".join(output))
            break     
    window.refresh() if window else None


def MainGui():

    file_column=[
        [sg.Text("Elige juego: ", font=(13))],
        [sg.Button("Ahorcado", key="HANG", size=(0, 1), font=(3)),
         sg.T('', size=(24, 4)),
         sg.Button("Buscaminas", key="MINE", size=(0, 1), font=(3)),
         sg.T('', size=(24, 4)),
         sg.Button("Agenda", key="SCHED", size=(0, 1), font=(3))],
        [sg.HorizontalSeparator()],
        [sg.Text('Scripting....', size=(40, 1))],
        [sg.T('Promt> '), sg.Input(key='-IN-', do_not_clear=False)],
		[sg.Button('Ejecutar', bind_return_key=True), sg.Button('Salir')]
    ]

    layout = [
        [sg.Column(file_column)]
    ]

    window = sg.Window(title="Suite-MiniGames", layout=layout,
                       size = (900, 700), margins = (100, 100))

    while True:
        event, values=window.read()
        if event == "HANG":
            p = Popen(["python3 src/test.py"], 
            shell = True, stdout = PIPE, stdin = PIPE)
            RunCommand(p, window=window)
        elif event == "MINE":
            RunCommand("pwd")
        elif event == "SCHED":
            RunCommand("Scheduler/SchedMain.py")
        elif event == 'Ejecutar':
            p.stdin.write(values['-IN-'].encode())
            RunCommand(p, window = window)
        elif event == "Salir" or event == sg.WIN_CLOSED:
            break
    window.Close()
