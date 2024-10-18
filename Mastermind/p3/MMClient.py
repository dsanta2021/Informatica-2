from socket import *
from subprocess import run as terminal
from time import sleep
import getopt, sys


class Client():                                             #Clase encargada de la conexion TCP y de la comunicacion con el servidor


    type = {}
    untype = {}
    buffer = ""
    GameOver: bool


    def __init__(self, serverName, serverPort):

        self.serverName = serverName
        self.serverPort = serverPort
        self.clientSocket = None

        self.type["Init"]       = "I"
        self.type["Turn"]       = "T"
        self.type["Error"]      = "E"
        self.type["GameOver"]   = "GO"
        self.type["Win"]        = "W"
        self.type["Key"]        = "K"
        self.type["SecretKey"]  = "SK"

        self.untype["I"]        = "Init"
        self.untype["T"]        = "Turn"
        self.untype["E"]        = "Error"
        self.untype["GO"]       = "GameOver"
        self.untype["W"]        = "Win"
        self.untype["K"]        = "Key"
        self.untype["SK"]       = "SecretKey"

        self.GameOver = False



    def Encoder(self, type: str, input):                #Genera mensajes para enviar
        buffer = self.type[type] + "#"
        match type:
            case "Init":
                buffer = buffer + input
            case "SecretKey":
                buffer = buffer + input
            case "Key":
                buffer = buffer + input
        return buffer



    def Decoder(self):         # Interpreta mensajes del servidor e imprime por pantalla

        content = self.buffer.split("#")
        content[0] = self.untype[content[0]]

        match content[0]:

            case "Init":
                message = content[1]
                print(message)
                print("")

            case "SecretKey":
                message = content[1]
                print(message)
                print("")


            case "Turn":
                Key = list(map(lambda x: content[x], range(1, 4+1)))
                currentTurn = content[5]
                EMatches = content[6]
                PMatches = content[7]
                print("")
                print(f"Tu turno: {currentTurn}")
                print(f"Tu combinación es: {Key}")
                print(f"Número de aciertos: {EMatches}")
                print(f"Número de semiaciertos: {PMatches}")
                print("")
                print("No te rindas!")
                print("")
                print("")
            case "Error":

                print("")
                match content[1]:
                    case "NumberOfTurnsError":
                        print("Se ha producido un error.")
                        print(f"Información sobre el error: error_Type:{content[1]}")
                        print("El numero de turnos configurado por defecto es 10.")
                    case "SecretKeyError":
                        print("Se ha producido un error.")
                        print(f"Información sobre el error: error_Type:{content[1]}")
                        print("Se ha configurado una clave secreta aleatoria por defecto.")
                    case "KeyError":
                        print("Se ha producido un error.")
                        print(f"Información sobre el error: error_Type:{content[1]}")
                        print("CLave incorrecta.")
                        print("Vuelve a intentarlo!")
                    case other:
                        print("Se ha producido un error.")
                        print("Información sobre el error: error_Type:UnknownError")
                print("")

            case "GameOver":
                self.GameOver = True
                sKey = list(map(lambda x: content[x], range(1, 4+1)))
                Key = list(map(lambda x: content[x], range(5, 8+1)))
                currentTurn = content[9]
                EMatches = content[10]
                PMatches = content[11]

                print("")
                print("")
                print("Vaya... Parece que has alcanzado el último turno.")
                print(f" Quizá {currentTurn} sean demasiado pocos turnos para ti. 🤣🤣🤣🤣🤣")
                print(f" La clave correcta era: {sKey}.")
                print(f"Tu combinación es: {Key}.")
                print(f"Aciertos: {EMatches}. Semiaciertos: {PMatches}.")
                print("")
                print("")
                input("Pulsa enter para continuar")
                terminal("clear")
                print("")
                print("")
                print("####   ##   #   #  ####       ####  #   #  ####   ## ")
                print("#     #  #  ## ##  #          #  #  #   #  #     #  #")
                print("# ##  ####  # # #  ####       #  #  #   #  ####  ### ")
                print("#  #  #  #  # # #  #          #  #   # #   #     #  #")
                print("####  #  #  #   #  ####       ####    #    ####  #  #")


            case "Win":
                MMkey = content[1]
                self.GameOver = True
                terminal("clear")
                print("")
                print("#    #  ####  #  #       #  #  #  ##  ##  # ")
                print(" #  #   #  #  #  #       #  #  #  ##  ##  # ")
                print("  ##    #  #  #  #       #  #  #  ##  # # # ")
                print("  ##    #  #  #  #        # # #   ##  #  ## ")
                print("  ##    ####  ####         ###    ##  #  ## ")
                print("")



    def connection(self):

        self.clientSocket = socket(AF_INET, SOCK_STREAM)
        self.clientSocket.connect((self.serverName, self.serverPort))


    def shipment(self, type: str, input):

        self.clientSocket.send(self.Encoder(type, input).encode())


    def catch(self):

        self.buffer = self.clientSocket.recv(1024).decode()


    def close(self):

        self.clientSocket.close()




class arguments():                                      #Clase encargada de interpretarlos argumentos introducidos en el terminal

    ip = "0.0.0.0"
    port = 9000
    name = ""

    nameError: bool
    portError: bool
    ipError: bool

    def __init__(self):
        (opts, args) = getopt.getopt(sys.argv[1:], "n:i:p:", ["name=", "ip=", "port="])
        for o, a in opts:
            if o in ("-n", "--name"):
                self.name = a
            elif o in ("-i", "--ip"):
                self.ip = a
            elif o in ("-p", "--port"):
                self.port = a
        self.nameError = False
        self.portError = False
        self.ipError = False




    def argumentError(self):

        if len(self.name) < 0 and len(self.name) > 100:
           self.nameError = True
        if len(self.ip) == 0:
            self.ipError =True
        else:
            try:
                self.port = int(self.port)
                if not self.port > 0:
                    self.portError = True
            except ValueError:
                self.portError = True




    def argumentRun(self):
        if self.nameError:
            print("Se ha producido un error.")
            print("error_Type:InvalidInput:type=name")
            input("Pulsa enter para continuar.")
            exit(1)
        if self.ipError:
            print("Se ha producido un error.")
            print("error_Type:InvalidInput:type=ip")
            self.ip = "127.0.0.1"
        if self.portError:
            print("Se ha producido un error.")
            print("error_Type:InvalidInput:type=port")
            self.port = 1234
        else:
            print("Argumentos correctos.")
        input("Pulsa enter para continuar.")







########################## E J E C U C I O N #####################################

terminal("clear")


arguments = arguments()

arguments.argumentError()
arguments.argumentRun()
tcpClient = Client(arguments.ip, arguments.port)
try:
    tcpClient.connection()
except:
    print("Se ha producido un error.")
    print("error_Type:ConectionError=ConectionRefused")
    input("Pulsa enter para continuar.")
    terminal("clear")
    exit(1)

terminal("clear")

print("")
print("")
print("##   ##    ###     ###   #######   ####   ####        @@   @@   @   @@    @   @@@@   ")
print("# # # #   #   #   #         #     #       #   #       @ @ @ @   @   @ @   @   @   @  ")
print("#  #  #   #####    ###      #      ####   ####        @  @  @   @   @  @  @   @   @  ")
print("#     #   #   #       #     #     #       #  #        @     @   @   @   @ @   @   @  ")
print("#     #   #   #    ###      #      ####   #   #       @     @   @   @    @@   @@@@   ")
print("")
print("                                                                                   ~By Hearts Punk Records")
print("")
print("")
input("Pulsa enter para continuar.")
terminal("clear")

                                                                            #Fase 1
tcpClient.shipment("Init",input("Introduce el número de turnos:"))
tcpClient.catch()
tcpClient.Decoder()
                                                                            #Fase 2
print("**Clave de colores**")
print("             Rojo     🔴  : Letra R")
print("             Azul     🔵  : Letra B")
print("             Amarillo 🟡  : Letra Y")
print("             Verde    🟢  : Letra G")
print("             Blanco   ⚪  : Letra W")
print("             Negro    ⚫  : Letra K")

tcpClient.shipment("SecretKey",input("Introduce la clave a adivinar (no escribas nada para hacerla aleatoria): "))
tcpClient.catch()
tcpClient.Decoder()
input("Pulsa enter para continuar.")
terminal("clear")
                                                                            #Fase 3
print("**Clave de colores**")
print("             Rojo     🔴  : Letra R")
print("             Azul     🔵  : Letra B")
print("             Amarillo 🟡  : Letra Y")
print("             Verde    🟢  : Letra G")
print("             Blanco   ⚪  : Letra W")
print("             Negro    ⚫  : Letra K")
while not tcpClient.GameOver:

    tcpClient.shipment("Key",input("Introduce una clave de colores:"))
    tcpClient.catch()
    tcpClient.Decoder()
    sleep(0.4)

input("Pulsa enter para cerrar el juego.")
terminal("clear")
tcpClient.close()

