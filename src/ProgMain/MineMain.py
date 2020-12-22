#Módulos
from src.ProgSupport import MineSupport as ms

movementsDone = []
mineSaved = 0

#Creación del escenario
selection = ms.FormatSelect("Elige número de filas y columnas (filas,columnas): ")
board = ms.BoardCreate(int(selection[0]), int(selection[1]))

#Colocación de minas
if len(movementsDone) == 0:
    mines = ms.FormatSelect("Elige número de minas: ")
BoardMined = ms.MineBoard(board, int(mines[0]))
minesCoord = ms.whereMines(BoardMined)

while True:
    #Seleccionar movimiento de juego
    selection = ms.FormatSelect("Elige movimiento (x,y): ")
    if (int(selection[0]), int(selection[1])) not in movementsDone:
        movementsDone.append((int(selection[0]), int(selection[1])))
        movement = ms.MinePosition(minesCoord, int(selection[0]), int(selection[1]))
    else:
        resultMessage = movement[1]

    #Modificar estado del tablero
    if len(movementsDone) == 1:
        BoardPlayed = ms.PrettyBoard(BoardMined, int(selection[0]), int(selection[1]), movement[0])
    else:
        BoardPlayed = ms.PrettyBoard(BoardPlayed, int(selection[0]), int(selection[1]), movement[0])

    #Printear estado del tablero
    print(BoardPlayed)
