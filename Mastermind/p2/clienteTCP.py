from socket import *

class TCPCliente():
    def __init__(self, serverName, serverPort):
        self.nombreServidor = serverName
        self.numeroPuerto = serverPort
        self.clienteSocket = None
        self.mensajeModificado = None
        self.jugador = None
        self.exit = True

    def connect(self):
        self.clienteSocket = socket(AF_INET, SOCK_STREAM)
        self.clienteSocket.connect((self.nombreServidor, int(self.numeroPuerto)))

    def enviar(self, mensaje):
        self.clienteSocket.send(mensaje.encode())

    def recibir(self):
        self.mensajeModificado = self.clienteSocket.recv(1024) #el 1024 es el tamaño del buffer en bits.
        return self.mensajeModificado.decode()

    def sendHead(self, head):
        match head:
            case 'START':
                turnos = input('Dame el número de turnos 🎲:')
                return head + '#' + str(turnos)
            case 'CIPHER':
                secretCode = input('Introduce la clave secreta con la que quieres jugar ↪ ')
                return head + '#' + secretCode
            case 'COMBI':
                combiPlay = input('Introduzca una combinación ➡ ')
                return head + '#' + combiPlay

    def reciveHead(self, head):
        text = head.split("#")
        print('')
        match text[0]:
            case 'START':
                if int(text[2]) < 1:
                    print(text[1])
                else:
                    print(text[1] + text[2])
                    self.exit = False  # Cambiamos la condición del buv¡cle para que salga de él
            case 'CIPHER':
                if text[1] == 'Combinación Secreta no válida🤡':
                    print(text[1])
                else:
                    print(text[1])
                    self.exit = False
            case 'ERROR':
                print(text[1])
            case 'TURN':
                print('Su turno es:', text[1])
                print('SU combinación es:', text[4])
                print('Número de aciertos:', text[2])
                print('Número de semiaciertos:', text[3])
            case 'WIN':
                print(text[1])
                print(f'🥇Ha logrado acertar la clave secreta {text[3]} en el turno {text[2]}🥇')
                print('')
                exit(-1)
            case 'FIN':
                print(text[1])
                print('¡La partida ha terminado!👻 Lo ha hecho en el turno', text[3])
                print('La clave secreta era:', text[2])
                print('')
                exit(-1)
        print('')

    def communication(self):
        if self.clienteSocket is None:
            self.connect()

        # Lo primero que mandas es el número de turnos: BEGIN
        while self.exit:
            message = self.sendHead('START')
            self.enviar(message)
            mr = self.recibir()  # Mensaje que recibe del servidor
            self.reciveHead(mr)  # Escribe si se ha establecido los turnos
        self.exit = True

        # Lo segundo que se manda es la clave secreta (CODE). combiCode si se quiere aleatoria
        while self.exit:
            message = self.sendHead('CIPHER')
            self.enviar(message)
            mr = self.recibir()  # Mensaje que recibe del servidor
            self.reciveHead(mr)  # Escribirá la clave secreta

        # Se mandarán varias combinaciones para intentar acertar la combinación secreta (COMBINATION)
        while True:
            message = self.sendHead('COMBI')
            self.enviar(message)
            mr = self.recibir()  # Mensaje que recibe del servidor
            self.reciveHead(mr)  # Escribirá la clave mandada, el nº de aciertos, semiaciertos y turno