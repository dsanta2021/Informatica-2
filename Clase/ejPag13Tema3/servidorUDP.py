from socket import *

serverPort = 12000

serverSocket = socket(AF_INET , SOCK_DGRAM)
serverSocket.bind (('',serverPort ))
print ("El servidor esta listo para ser usado")

while True:
    mensaje, dirCliente = serverSocket .recvfrom (2048)
    mensj_mod = mensaje.decode ().upper ()
    serverSocket .sendto( mensj_mod.encode () ,dirCliente )