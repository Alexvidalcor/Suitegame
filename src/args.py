import argparse

def parseator():
    parser = argparse.ArgumentParser()
    parser.add_argument("-h", "--hang", type=str,help="Ejecutar juego de arhorcado")
    parser.add_argument("-m","--mine", type=str,help="Ejecutar juego de buscaminas")
    parser.add_argument("-s","--sched", type=str,help="Ejecuta la aplicación de agenda")
    args = parser.parse_args()

    return args