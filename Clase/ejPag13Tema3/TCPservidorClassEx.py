from socket import *

class TCPservidorClassEx():
    def __init__(self,servePort):
        self.puerto = servePort
        self.serverSocket = None

    def crear(self):
        self.serverSocket = socket(AF_INET, SOCK_STREAM)
        self.serverSocket.bind(('localhost',self.puerto))
        self.serverSocket.listen(1) #solo admite uno, los demás los descarta
        print("El servidor esta listo para ser usado")

    def getSocket (self):
        return self.__socket

    def comunicacion(self):
        while True:
            clienteSocket, direccion = self.serverSocket.accept()
            mensaje = clienteSocket.recv(1024)
            mayuscula = mensaje.decode().upper()
            clienteSocket.send(mayuscula.encode())
            clienteSocket.close()