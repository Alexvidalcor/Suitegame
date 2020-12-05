#Módulos
from src.generation import *
from src.extras import *

movementsDone = []
mineSaved = 0
#Creación del escenario
selection = FormatSelect("Elige número de filas y columnas (filas,columnas): ")
board = BoardCreate(int(selection[0]), int(selection[1]))

#Colocación de minas
if len(movementsDone) == 0:
    mines = FormatSelect("Elige número de minas: ")
BoardMined = MineBoard(board, int(mines[0]))
minesCoord = whereMines(BoardMined)

while True:
    #Seleccionar movimiento de juego
    selection = FormatSelect("Elige movimiento (x,y): ")
    if (int(selection[0]), int(selection[1])) not in movementsDone:
        movementsDone.append((int(selection[0]), int(selection[1])))
        movement = MinePosition(minesCoord, int(selection[0]), int(selection[1]))
    else:
        resultMessage = movement[1]

    #Modificar estado del tablero
    if len(movementsDone) == 1:
        BoardPlayed = PrettyBoard(BoardMined, int(selection[0]), int(selection[1]), movement[0])
    else:
        BoardPlayed = PrettyBoard(BoardPlayed, int(selection[0]), int(selection[1]), movement[0])

    #Printear estado del tablero
    print(BoardPlayed)
