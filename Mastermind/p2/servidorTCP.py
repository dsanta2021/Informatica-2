from socket import *
from socketHilo import *

class TCPservidor():
    def __init__(self, serveName, servePort):
        self.puerto = servePort
        self.ip = serveName
        self.serverSocket = None

    def crear(self):
        self.serverSocket = socket(AF_INET, SOCK_STREAM)
        self.serverSocket.bind((self.ip, int(self.puerto)))
        self.serverSocket.listen(1)  # solo admite uno, los demás los descarta
        print("El servidor esta listo para ser usado")

    def disconnectSocket(self):
        self.serverSocket.close()
        self.serverSocket = None

    def getSocket(self):
        return self.serverSocket

    def comunication(self):
        while True:
            clientSocket, direccion = self.serverSocket.accept()
            threadsocket = socketHilo(clientSocket, direccion)
            print("conexion desde:", direccion)
            threadsocket.start()
