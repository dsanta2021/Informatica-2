from socket import *
from ThreadingSocket import socketThread
import sys, getopt

##Cerrar conexión al terminar

class TCPServer:                #Gestiona la conexión TCP

    def __init__(self, serverName, serverPort): #añadir ip
        self.serverName = serverName
        self.serverPort = serverPort
        self.serverSocket = None


    def activate(self):
        self.serverSocket = socket(AF_INET, SOCK_STREAM)
        self.serverSocket.bind((self.serverName, self.serverPort))
        self.serverSocket.listen (1) # Numero de solicitudes en cola admitidas, resto se descartan


    def comunication(self):
        while True:
            (clientsocket, address) = self.serverSocket.accept()
            threadsocket = socketThread(clientsocket, address)
            print(f"Conexión desde: {address}")
            try:
                threadsocket.start()


            except ValueError:
                self.close()


    def close(self):
        self.serverSocket.close()



class arguments():              #Clase encargada de leer los argumentos escritos en el terminal

    ip = "0.0.0.0"
    port = 9000

    selfportError: bool
    ipError: bool

    def __init__(self):
        (opts, args) = getopt.getopt(sys.argv[1:], "i:p:", ["ip=", "port="])
        for o, a in opts:
            if o in ("-i", "--ip"):
                self.ip = a
            elif o in ("-p", "--port"):
                self.port = a

        self.portError = False
        self.ipError = False


    def argumentError(self):

        if len(self.ip) == 0:
            self.ipError =True
        else:
            try:
                self.port = int(self.port)
                if not self.port > 0:
                    self.portError = True
            except ValueError:
                self.portError = True


    def argumentRun(self):                      #Gestion de errores
        if self.ipError:
            print("Error:InvalidInput_type=ip")
            self.ip = "127.0.0.1"
        if self.portError:
            print("Error:InvalidInput_type=port")
            self.port = 1234
        else:
            print("Argumentos correctos.")



########################## E J E C U C I O N #####################################




arguments = arguments()
arguments.argumentError()
arguments.argumentRun()

tcpServer = TCPServer(arguments.ip, arguments.port)
tcpServer.activate()
print ("El servidor esta listo para ser usado")
tcpServer.comunication()
tcpServer.close()
