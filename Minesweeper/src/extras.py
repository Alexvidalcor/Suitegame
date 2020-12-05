
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










