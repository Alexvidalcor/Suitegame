#Importación de librerías
import os
import sys

#Importación de módulos

if __name__ != "__main__":
    import src.HangSupport as hg
else:
    import HangSupport as hg

#Elección de palabra inicial
wordChosen = hg.WordGenerator()
resultCreate = ["_" for ele in range(len(list(wordChosen)))]
hangmanGen = hg.SelectHangman()
hangman = next(hangmanGen)
print(f"{hangman[1]} \n {resultCreate}")

while True:

    #Elección de letra
    letterChosen = input("Introduce letra: ")

    #Invocación de resultados
    simplifyVars = [letterChosen, wordChosen, resultCreate, hangman, hangmanGen]
    hangman, resultCreate, statusGame = hg.ShowResults(*simplifyVars, correctCheck=hg.GameCheck(*simplifyVars))
    
    #Chequeo de finalización de juego
    if hg.endGame(statusGame, wordChosen) == True:
        sys.exit(0)
    
    #Printeo de resultados
    print(f"{hangman[1]} \n {resultCreate}")

    



