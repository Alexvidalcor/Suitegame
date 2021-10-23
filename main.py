
#Importación de librerías
import os

from src.args import parseator
from src.Hangman.HangMain import *
from src.Minesweeper.MineMain import *
from src.Scheduler.SchedMain import *

#Inicio de programa
if __name__ == "__main__":
    
    args = parseator()

    print("Bienvenid@ a esta recopilación de utilidades escritas en Python")
    print("Ejecuta el programa con el argumento '--h' para más información")

    if args.hangman:
        print("\n-------------------\nEjecutando Hangman\n-------------------\n")
        Hangman()
    
    if args.minesweeper:
        print("\n-------------------\nEjecutando Minesweeper\n-------------------\n")
        Minesweeper()

    if args.scheduler:
        print("\n-------------------\nEjecutando Scheduler\n-------------------\n")
        Scheduler()
        

