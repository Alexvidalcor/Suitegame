#Importación de librerías
import os
import sys

#Importación de módulos
from src.ProgSupport import HangSupport

#Elección de palabra inicial
wordChosen = WordGenerator()
resultCreate = ["_" for ele in range(len(list(wordChosen)))]
hangmanGen = SelectHangman()
hangman = next(hangmanGen)
print(f"{hangman[1]} \n {resultCreate}")

while True:

    #Elección de letra
    letterChosen = input("Introduce letra: ")

    #Invocación de resultados
    simplifyVars = [letterChosen, wordChosen, resultCreate, hangman, hangmanGen]
    hangman, resultCreate, statusGame = ShowResults(*simplifyVars, correctCheck=GameCheck(*simplifyVars))
    
    #Chequeo de finalización de juego
    if endGame(statusGame, wordChosen) == True:
        sys.exit(0)
    
    #Printeo de resultados
    print(f"{hangman[1]} \n {resultCreate}")

    



