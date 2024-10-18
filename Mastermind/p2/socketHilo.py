import threading
from MasterMind03 import MasterMindGame

class socketHilo(threading.Thread):
    def __init__(self, clientSocket, direccion):
        threading.Thread.__init__(self)
        self.socket = clientSocket
        self.direccion = direccion
        self.secretCode = ''
        self.maxTurn = 0
        self.exit = True #Condición para los bucles

    def sendHead(self, cabecera, game:MasterMindGame):
        head = cabecera.split("#")
        match head[0]:
            case 'START':
                if self.maxTurn >= 1:
                    self.exit = False #Cambiamos la condición de salida del primer bucle para salir de él
                    return head[0] + '#' + 'Turnos establecidos en ' + '#' + str(self.maxTurn)
                else:
                    return head[0] + '#' + 'Mira que te he avisado... hay que poner un número válido🙄' + '#' + str(self.maxTurn)
            case 'CIPHER':
                if self.secretCode == 'nocombiCode' or self.secretCode == '':
                    game.maxTurns = self.maxTurn  #Para inicializar los turnos en MM
                    return head[0] + '#' + 'Clave secreta inicializada de forma aleatoria'
                else:
                    try:
                        sC = game.toMasterMindColorCombination(self.secretCode)
                        self.exit = False #Cambiamos la condición de salida del primer bucle para salir de él
                        return head[0] + '#' + str(sC)
                    except:
                        return head[0] + '#' + 'Combinación Secreta no válida🤡'
            case 'ERROR':
                match head[1]:
                    case 'ERROR3':
                        return head[0] + '#' + 'El número de turnos no es un número🧐 '
                    case 'ERROR1':
                        return head[0] + '#' + '❌ Combinación de colores incorrecta ❌'
                    case 'ERROR2':
                        return head[0] + '#' + '🚨 Tamaño de combinación no válido 🚨'
            case "TURN":
                return head[0] + '#' + str(game.currentTurn) + '#' + str(game.nMatches) + '#' + str(game.sMatches) + '#' + str(game.pGuess)
            case "WIN":
                return head[0] + '#' + '¡¡🎉🎉Increíble🎉🎉!! ¡Felicidades, ha ganado!🥳' + '#' + str(game.currentTurn) + '#' + str(game.secretCode)
            case 'FIN':
                return head[0] + '#' + '💀¡GAME OVER!💀' + '#' + str(game.secretCode) + '#' + str(game.currentTurn)

    def reciveHead(self, code, game:MasterMindGame):
        message = code.split("#")
        match message[0]:
            case 'START':
                try:
                    self.maxTurn = int(message[1])
                    return message[0]
                except:
                    return 'ERROR#ERROR3'
            case 'CIPHER':
                self.secretCode = message[1] #Ponemos la variable con la combinación que manda el clinete
                return message[0]
            case 'COMBI':
                return game.newTurn(message[1]) #Inicializa newTurn para mandar las cabeceras a la función send.

    def run(self):
        game = MasterMindGame()  # Inicializar el juego MM

        #Esto para el número de turnos (BEGIN)
        while self.exit:
            message = self.socket.recv(1024).decode()
            rmessage = self.reciveHead(message, game)
            smessage = self.sendHead(rmessage, game).encode()
            self.socket.send(smessage)
        self.exit = True #Sale del bucle como False. Se vuelve a poner como True para que se meta en el siguiente bucle

        #Esto para la clave secreta (CODE)
        while self.exit:
            message = self.socket.recv(1024).decode()
            rmessage = self.reciveHead(message, game)
            smessage = self.sendHead(rmessage, game).encode()
            self.socket.send(smessage)

        #Para las combinaciones que se mandan para acertar la clave secreta
        game = MasterMindGame(self.secretCode)  # Inicializar el juego con la clave secreta
        game.maxTurns = self.maxTurn  #Metemos el número de trunos en el MM con el valor de self.secretCode
        while True:
            message = self.socket.recv(1024).decode()
            rmessage = self.reciveHead(message, game)
            smessage = self.sendHead(rmessage, game).encode()
            self.socket.send(smessage)