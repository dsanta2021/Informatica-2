#programa igual que clienteTCP pero con programación orientada a objetos
from socket import *


class TCPclienteClassEx():
    def __init__(self, serverName, serverPort):
        self.nombreServidor = serverName
        self.numeroPuerto = serverPort
        self.clienteSocket = None

    def connect(self):
        self.clienteSocket = socket(AF_INET, SOCK_STREAM)
        self.clienteSocket.connect((self.nombreServidor, self.numeroPuerto))

    def enviar(self, mensaje):
        self.clienteSocket.send(mensaje.encode())

    def recibir(self):
        mensajeModificado = self.clienteSocket.recv(1024) #el 1024 es el tamaño del buffer en bits.
        return mensajeModificado.decode()

    def cerrarConexion(self):
        self.clienteSocket.close()
        
