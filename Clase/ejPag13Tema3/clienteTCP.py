from socket import *

serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket ( AF_INET , SOCK_STREAM )
clientSocket.connect ((serverName , serverPort))

mensaje = input ('Introduzca la frase en minusculas: ')

clientSocket.send(mensaje.encode ())

mensajeModificado = clientSocket.recv (1024)
print ("Mensaje desde el servidor: ", mensajeModificado .decode ())
clientSocket .close ()