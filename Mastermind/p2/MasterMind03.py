import random

# esqueleto inicial
class MasterMindGame:
    # declaramos las variables que vamos a utilizar

    MMC = {}  # diccionario de colores válidos.

    secretCode = []  # código secreto que tenemos que adivinar.

    validColors = "rgybkw"  # colores mastermind permitidos

    maxTurns = 0  # máximo número de turnos para acertar la clave.
    currentTurn = 0  # turno actual.
    sMatches = 0
    nMatches = 0
    pGuess = []

    # construimos la función para iniciar la clase
    def __init__(self, combiCode: str = "nocombiCode"):

        # El plugin que utilizo en el programa es el que os debe Daniel, que me dijo como se llamaba.
        # Este plugin se llama "Yet another emoji support" y se usa poniendo ":" y el nombre del emoji.

        # iniciamos el diccionario de colores
        self.MMC["red"] = "💔" # El único problema que tiene el plugin es que no hay un corazón rojo, sino que está roto. Pero para lo que lo queremos sirve.
        self.MMC["green"] = "💚"
        self.MMC["yellow"] = "💛"
        self.MMC["blue"] = "💙"
        self.MMC["black"] = "🖤"
        self.MMC["white"] = "🤍"

        if combiCode == 'nocombiCode':
            self.secretCode = self.randomCode(4)
        else:
            try:
                self.secretCode = self.toMasterMindColorCombination(combiCode)
            except:
                self.secretCode = self. randomCode(4)

    def randomCode(self, n: int):  # genera un código aleatorio
        colorsList = list(self.validColors)
        passCode = random.choices(colorsList, k=n)
        return self.toMasterMindColorCombination(passCode)

    def MasterMindColor(self, color:str):  # convertir cadenas en colores

        rcolor = "Color no encontrado."

        if color == "r" or color == "R" or color == "💔":
            rcolor = self.MMC["red"]
        elif color == "g" or color == "G" or color == "💚":
            rcolor = self.MMC["green"]
        elif color == "b" or color == "B" or color == "💙":
            rcolor = self.MMC["blue"]
        elif color == "y" or color == "Y" or color == "💛":
            rcolor = self.MMC["yellow"]
        elif color == "k" or color == "K" or color == "🖤":
            rcolor = self.MMC["black"]
        elif color == "w" or color == "W" or color == "🤍":
            rcolor = self.MMC["white"]
        else:
            raise KeyError(rcolor)

        return rcolor

    def toMasterMindColorCombination(self, combi:list):  # obtener una cadena de colores mastermind
        return list(map(lambda n: self.MasterMindColor(n), combi))

    def countExactMatches(self, mmCombi): #compara la combinación del jugador con la generada y cuenta los aciertos
        compResult = list(map(lambda x, y: x == y, mmCombi, self.secretCode))

        count = len(list(filter(lambda x: x is True, compResult)))
        return count

    def countPartialMatches(self, mmCombi: list):

        partialMatches = 0

        trueMatches = tuple(map(lambda x, y: (x, x == y), self.secretCode, mmCombi))  # guarda en diferentes tuplas el valor de secretCode (en orden, es decir, cuatro tupla. Una con cada posición de secretCode) y si coincide o no (True o False) con el código metido.
        guess = list(map(lambda x, y: (y, x == y), self.secretCode, mmCombi))  # guarda las tuplas anteriorers en una sola lista.

        def chkMatch(x):  # comprueba los semiaciertos y aciertos
            comprobado = False

            if guess.__contains__(x) and not x[1]:  # si la tupla contiene en el segundo elemnto un True, se considera acierto y en entra en el if. Cuando es False el segundo elemento siq ue entra en el if porque es un candidato a semiacierto.
                index = guess.index(x)  # index coge la posición numérica del array
                if trueMatches[index][1] == False:  # si el segundo elemento de la tupla en la posición de index es False entra en el if
                    guess[index] = (x[0], True)  # entonces en la segunda lista (guess) se campiaba la tupla en esa posicón.
                    comprobado = True

            return (x[0], comprobado)

        tsMatches = tuple(map(lambda x: chkMatch(x), trueMatches))

        for x in tsMatches:  # bucle que va sumando el número de semiaciertos
            if x[1] == True:
                partialMatches += 1

        return partialMatches

    def newTurn(self, guess: list):
        # self.pGuess = []
        bGuestMatch = False

        # comprobar si es una combinación válida
        try:
            self.pGuess = self.toMasterMindColorCombination(guess)
        except:
            return 'ERROR' + '#' + 'ERROR1'

        # comprobamos si el número de colores de la combinación es el adecuado
        lSecretCode = len(self.secretCode)
        if len(self.pGuess) != lSecretCode:
            return 'ERROR' + '#' + 'ERROR2'

        self.currentTurn += 1
        self.nMatches = self.countExactMatches(self.pGuess)
        self.sMatches = self.countPartialMatches(self.pGuess)

        if lSecretCode == self.nMatches:
            return 'WIN#'

        # Comprobamos si hemos agotado los turnos o hemos acertado
        if self.currentTurn == self.maxTurns or bGuestMatch:
            return 'FIN#'

        return 'TURN#'