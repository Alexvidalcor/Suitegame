
#Importación de librerías
import random as rd

'''
Generar un único número aleatorio. 
Length = True --> Devuelve número aleatorio de 0 a len(filas)
Length = False --> Devuelve número aleatorio de 0 a len(columnas)
'''
def RandomBoard(board, length=False):
    if length==True:
        return rd.randint(0, len(board)-1)
    if length== False:
        return rd.randint(0,len(board[0])-1)

#Copiar tablero inmutable a mutable. Devuelve [[Tablero mutable]]
def BoardCopy(board):
    newBoard = []
    temp = []
    for element in board:
        for element2 in element:
            temp.append(element2)
        newBoard.append(temp)
        temp=[]
    return newBoard

#Extraer coordenadas de la mina. Devuelve [(fila, columna)] de minas
def whereMines(board):
    coordMines = []
    for row, element in enumerate(board):
        for column, element2 in enumerate(element):
            if element2 == "X":
                coordMines.append([row, column])
    return coordMines





#Procesar un input genérico. Devuelve resultado del input formateado.
def FormatSelect(question):
    return input(question).replace(", ", ",").replace(" ,", ",").split(",")

#Creación del escenario de juego. Devuelve [["Tablero sin minas"]]
def BoardCreate(columns=4, rows = 4):
    return [["-" for element in range(columns)]]*rows

#Colocación de las minas. Devuelve [["Tablero Minado"]]
def MineBoard(board ,mineNumber = 1):
    newBoard = BoardCopy(board)
    count = 0
    while count < mineNumber:
        randomColumn = RandomBoard(newBoard,length=False)
        randomRow = RandomBoard(newBoard,length=True)
        if newBoard[randomRow][randomColumn] ==  "X":
            continue
        newBoard[randomRow][randomColumn] = "X"
        count +=1
    return newBoard

#Analiza el movimiento del jugador en función de las minas. Devuelve "mensaje de resultado"
def MinePosition(minesCoord,x,y):
    playerCoord = [x,y]
    results = []
    for element in minesCoord:
        results.append([x1 - x2 for (x1, x2) in zip(playerCoord, element)])
    distanceMine = sum([abs(element) for element in min(results)])

    if distanceMine == 0:
        ending = (distanceMine,"Caíste en la mina")
    elif distanceMine >=1 and distanceMine <=3:
        ending = (distanceMine,f"Estás a {distanceMine} casillas de una mina")
    elif distanceMine >3:
        ending = ("OK", "Zona segura")

    return ending

#Prettyficar lista de listas. Devuelve tablero bonito.
def PrettyBoard(board, row, column, minePos, hideMines = True):
    if hideMines == True:
        for position1, element1 in enumerate(board):
            for position2, element2 in enumerate(element1):
                if element2 == "X":
                    board[position1][position2] = "-"
                if position1 == row and position2 == column:
                    board[position1][position2] = minePos
        
        return '\n'.join(['\t'.join([str(cell) for cell in row])for row in board])



