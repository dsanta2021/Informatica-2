from socket import *

serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket ( AF_INET , SOCK_DGRAM )

mensaje = input ('Introduzca la frase en minusculas: ')

clientSocket.sendto(mensaje.encode(), (serverName , serverPort ))

mensjMod , dirServidor = clientSocket.recvfrom (2048)

print (mensjMod.decode ())