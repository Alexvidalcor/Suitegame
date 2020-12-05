#Importación de librerías
import argparse

#Importación de módulos
from src.args import *

#Esta función proporciona soporte a los parámetros de la consola:
def Parser():

    parser = argparse.ArgumentParser()
    parser.add_argument("-a","--ahorcado",action='store_true',dest='hang',help="Inicia el minijuego del ahorcado")
    parser.add_argument("-b","--buscaminas", action='store_true',dest='mine',help="Inicia el minijuego del buscaminas")
    parser.add_argument("-v",'--version', action='version',version='MiniGames_Suite 1.0')
    args = parser.parse_args()

    return args