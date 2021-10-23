import argparse

'''
IMPORTANTE REVISAR DOCS DE ARGPARSE: https://docs.python.org/3/library/argparse.html
'''
nameProg = "SuiteMinigames"
usageProg = "%(prog)s [options]"
epilogProg = "See you soon"
# defaultProg = "-hang"
descProg = "Testing description"


def parseator():
    parser = argparse.ArgumentParser(prog = nameProg, 
    					usage = usageProg, 
    					epilog = epilogProg,
    					description=descProg
    					)
    parser.add_argument("-hang", action='store_true',dest="hangman",help="Ejecutar juego de ahorcado")
    parser.add_argument("-mine", action='store_true', dest="minesweeper", help="Ejecutar juego de buscaminas")
    parser.add_argument("-sched", action='store_true', dest="scheduler", help="Ejecuta la aplicación de agenda")
    args = parser.parse_args()  

    return args
