#Importación de librerías
import requests
from bs4 import BeautifulSoup
import re

#Generador que devuelve ahorcados
def SelectHangman():
    hangmans = ['''
    +---+
    |   |
        |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|\  |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|\  |
    /    |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|\  |
    / \  |
        |
    =========''']

    for pos, element in enumerate(hangmans):
        yield pos, element
     

def WordGenerator():
    page = requests.get("https://www.palabrasaleatorias.com/?fs=1&fs2=0&Submit=Nueva+palabra")
    soup = BeautifulSoup(page.content, 'html.parser')
    wordSearch = soup.find('div', style="font-size:3em; color:#6200C5;").get_text()
    wordFormat = re.findall(r'[A-Z][a-z]+\b', wordSearch)[0]

    return wordFormat


#Comprueba si letra es errónea o no. También determina si fin del juego
#Devuelve (Error Letra (Bool), Fin de juego (Bool))
def GameCheck(letter, word, result, counter, secret):
    if letter.lower() in word.lower() and letter.lower not in result:
        correct = True
        if "_" not in result:
            ending = True
        else:
            ending = False
    else:
        correct = False
        if counter[0] == 6:
           ending = True
        else:
            ending = False
        
    return (correct, ending)


#Devuelve resultados totales de la jugada
def ShowResults(letter, word, result, hangman, hangmanGen, correctCheck=()):
    
    if correctCheck[0] == False and correctCheck[1] ==True:
        return (hangman, result, True)
    if correctCheck[0] == False and correctCheck[1] ==False:
        return (next(hangmanGen), result, False)
    elif correctCheck[0] == True:
        try:
            if correctCheck[1] == True:
                return (hangman, result, True)
            result[word.index(letter.lower())] = letter
            return (hangman, result, False)
        except ValueError:
            result[0] = letter
            return (hangman, result, False)

#Resuelve el final del juego. Devuelve reinicio de juego o break total.
def endGame(statusGame, finalWord):
    if statusGame == True:
            print(f"Juego Terminado, la palabra era: {finalWord}")
            resetGame = input("¿Iniciar nueva partida? (S/N): ")
            if resetGame.lower() == "n":
                print("Gracias por jugar")
                return True
            elif resetGame.lower() == "s":
                os.execv(sys.executable, ['python'] + sys.argv)
#Generador que devuelve ahorcados
def SelectHangman():
    hangmans = ['''
    +---+
    |   |
        |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|\  |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|\  |
    /    |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|\  |
    / \  |
        |
    =========''']

    for pos, element in enumerate(hangmans):
        yield pos, element
     

def WordGenerator():
    page = requests.get("https://www.palabrasaleatorias.com/?fs=1&fs2=0&Submit=Nueva+palabra")
    soup = BeautifulSoup(page.content, 'html.parser')
    wordSearch = soup.find('div', style="font-size:3em; color:#6200C5;").get_text()
    wordFormat = re.findall(r'[A-Z][a-z]+\b', wordSearch)[0]

    return wordFormat


#Comprueba si letra es errónea o no. También determina si fin del juego
#Devuelve (Error Letra (Bool), Fin de juego (Bool))
def GameCheck(letter, word, result, counter, secret):
    if letter.lower() in word.lower() and letter.lower not in result:
        correct = True
        if "_" not in result:
            ending = True
        else:
            ending = False
    else:
        correct = False
        if counter[0] == 6:
           ending = True
        else:
            ending = False
        
    return (correct, ending)


#Devuelve resultados totales de la jugada
def ShowResults(letter, word, result, hangman, hangmanGen, correctCheck=()):
    
    if correctCheck[0] == False and correctCheck[1] ==True:
        return (hangman, result, True)
    if correctCheck[0] == False and correctCheck[1] ==False:
        return (next(hangmanGen), result, False)
    elif correctCheck[0] == True:
        try:
            if correctCheck[1] == True:
                return (hangman, result, True)
            result[word.index(letter.lower())] = letter
            return (hangman, result, False)
        except ValueError:
            result[0] = letter
            return (hangman, result, False)

#Resuelve el final del juego. Devuelve reinicio de juego o break total.
def endGame(statusGame, finalWord):
    if statusGame == True:
            print(f"Juego Terminado, la palabra era: {finalWord}")
            resetGame = input("¿Iniciar nueva partida? (S/N): ")
            if resetGame.lower() == "n":
                print("Gracias por jugar")
                return True
            elif resetGame.lower() == "s":
                os.execv(sys.executable, ['python'] + sys.argv)