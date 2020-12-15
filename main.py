
#Importación de librerías
import os 
from src.args import *

#Importación de juegos
from src.ProgMain import *

#Configuración de Argparse:
args = Parser()

#Establecemos la ruta actual del archivo como principal:
current_dir = os.path.dirname(os.path.realpath(__file__))

#Configuración de parseo
if args.mine == True:
    execfile("Hangman/Hangman.py")
elif args.hang == True:
    execfile("Minesweeper/Minesweeper.py")

