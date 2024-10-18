import random


# esqueleto inicial
class MasterMindGame:
    # declaramos las variables que vamos a utilizar

    keyLenght = 4
    MMC = {}  # diccionario de colores válidos.

    secretCode = []  # código secreto que tenemos que adivinar.
    RandomCode = False
    keyToTest = []

    validColors = "rgybkw"  # colores mastermind permitidos

    maxTurns = 10  # máximo número de turnos para acertar la clave.
    currentTurn = 0  # turno actual.
    GameOver = False

    partialMatches = 0
    exactMatches = 0

    error = ""

    # construimos la función para iniciar la clase
    def __init__(self, combiCode: str = "" , key = 0, turns = 0):
        # iniciamos el diccionario de colores
        self.MMC["red"]     = "🔴"
        self.MMC["green"]   = "🟢"
        self.MMC["yellow"]  = "🟡"
        self.MMC["blue"]    = "🔵"
        self.MMC["black"]   = "⚫"
        self.MMC["white"]   = "⚪"

        # if key > 0:
        #     self.keyLenght = key
        if turns > 0:
             self.maxTurns = turns

        if combiCode == "":
            self.secretCode = self.randomCode(self.keyLenght)


        else:
            try:
                self.secretCode = self.toMasterMindColorCombination(list(combiCode))
            except:
                self.secretCode = self.randomCode(self.keyLenght)
                self.error = "SecretKeyError"






    def randomCode(self, n: int):   # genera un código aleatorio

        colorlist = list(self.validColors)
        passCode = random.choices(colorlist, k=n)

        self.RandomCode = True

        return self.toMasterMindColorCombination(passCode)



    def MasterMindColor(self, color: str):  # convertir cadenas en colores
        rcolor = "Color no encontrado."

        if   color == "r" or color == "R" or color == "🔴":
             rcolor = self.MMC["red"]
        elif color == "g" or color == "G" or color == "🟢":
             rcolor = self.MMC["green"]
        elif color == "b" or color == "B" or color == "🔵":
             rcolor = self.MMC["blue"]
        elif color == "y" or color == "Y" or color == "🟡":
             rcolor = self.MMC["yellow"]
        elif color == "k" or color == "K" or color == "⚫":
             rcolor = self.MMC["black"]
        elif color == "w" or color == "W" or color == "⚪":
             rcolor = self.MMC["white"]
        else:
            self.error = "ColorError"

        return rcolor



    def toMasterMindColorCombination(self, combi: list):  # obtener una cadena de colores mastermind
        return list(map(lambda n: self.MasterMindColor(n), combi))




    def countExactMatches(self, keyToTest: list,):
        compResult = list(map(lambda x, y: x == y, keyToTest, self.secretCode))     #Crea una lista con el resultado bool de comparar cada elemento de las listas
        count = len(list(filter(lambda x: x is True, compResult)))      #Devuelve el número de valores True
        self.exactMatches = count



    def countPartialMatches(self, keyToTest: list):   #Una implementacion un tanto rebuscada.
        #Creo dos listas auxiliares para manipularlas en el proceso, y de primeras elimino los aciertos de ambas.

        count = 0       #variable que almacena la cuenta
        both = list(map(lambda x, y: (x, y), keyToTest, self.secretCode))   #Agrupo cada elemento de las listas originales en una dupla, y dichas duplas en esta lista.
        bothWithoutsExactMatches    = list(filter(lambda x: x[0] is not x[1], both))   #Filtro las duplas que tengan elementos iguales (aciertos)
        keyWithoutExactMatches      = list(map(lambda x: x[0], bothWithoutsExactMatches))    #Desempaqueto las duplas en dos listas
        codeWithoutExactMatches     = list(map(lambda x: x[1], bothWithoutsExactMatches))

        for key in keyWithoutExactMatches:      #Comparo cada elemento de key con todos los elementos de code
            for code in codeWithoutExactMatches:
                if key == code:     #Cuando un elemento coincide tenemos un semiacierto que incrementa count en 1.
                    count += 1
                    codeWithoutExactMatches.remove(code)    #Este color puede darnos resultados duplicados en el futuro, y ya no es necesario
                    break   #Por las mismas razones se debe salir del bucle

        self.partialMatches = count    #Al final de este proceso, count ha almaceado todos los semiaciertos








    def newturn(self, Key):                         #NewTurn ahora devuelve las cabeceras y almacena los errores que se generan en el programa
        self.error = ""

        try:
             self.keyToTest = self.toMasterMindColorCombination(Key)
             self.countExactMatches(self.keyToTest)
             self.countPartialMatches(self.keyToTest)
        except:
            return "Error"

        if self.error != "":
            self.error = "KeyError"
            return "Error"

        if len(self.keyToTest) != self.keyLenght:
            self.error = "KeyError"
            return "Error"

        self.currentTurn += 1
        if self.keyToTest == self.secretCode:
            self.currentTurn = self.maxTurns
            self.GameOver = True
            return "Win"

        if self.currentTurn == self.maxTurns:
            self.GameOver = True
            return "GameOver"

        return "Turn"


