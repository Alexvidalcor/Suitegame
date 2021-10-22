import argparse

'''
IMPORTANTE REVISAR DOCS DE ARGPARSE: https://docs.python.org/3/library/argparse.html
'''
nameProg = "SuiteMinigames"
usageProg = "%(prog)s [options]"
epilogProg = "See you soon"
defaultProg = "-hang"
descProg = "Testing description"


def parseator():
    parser = argparse.ArgumentParser(prog = nameProg, 
    					usage = usageProg, 
    					epilog = epilogProg,
    					description=descProg
    					)
    parser.add_argument("-hang", type=str,help="Ejecutar juego de arhorcado")
    parser.add_argument("-mine", type=str,help="Ejecutar juego de buscaminas")
    parser.add_argument("-sched", type=str,help="Ejecuta la aplicación de agenda")
    parser.add_argument("-help", "--h", type=str,help="Mostrar la ayuda")
    args = parser.parse_args()  

    return args
