import getopt
import sys
from clienteTCP import TCPCliente
from time import sleep
from subprocess import run as implement

def conseguirArgumentos():
    ip = "127.0.0.1"
    port = 1234
    nombreJugador = ''
    opts , args = getopt.getopt(sys.argv [1:] ,"i:p:n:", ["ip=", "port=", "nombreJugador="])
    for o, a in opts:
        if o in ("-i", "--ip"):
            ip = a
        elif o in ("-p", "--port"):
            port = a
        elif o in ("-n", "--nombreJugador"):
            nombreJugador = a
    return ip , port, nombreJugador

def comprobarArgumentos (ip , port, nombreJugador):
    port_ok = True
    ip_ok = True
    nombreJugador_ok = True
    try:
        port = int(port)
    except ValueError :
        port_ok = False
    if len(ip) < 7:
        ip_ok = False
    if len(nombreJugador) == 0:
        nombreJugador_ok = False
    return ip_ok , port_ok, nombreJugador_ok


##### MAIN #####
ip, port, nombreJugador = conseguirArgumentos()
ip_ok, port_ok, nombreJugador_ok = comprobarArgumentos(ip, port,nombreJugador)

if not ip_ok:
    print('Error de ejecución de la aplicación. Debe usar el parámetro -i o --ip= <dirección IP que desee usar>')
if not port_ok:
    print('Error de ejecución de la aplicación. Debe usar el parámetro -p o --port= <puerto que desee usar>')
if not nombreJugador_ok:
    print('Error de ejecución de la aplicación. Debe usar el parámetro -n o --nombreJugador= <ID que quiera utilizar>')
    exit(-1)

### Especie de MENU con las reglas y colores ###
implement('clear')
print(f'¡{nombreJugador} 🙋 Bienvenido al fantástico juego MasterMind!')
sleep(2)
print('')
print('Para empezar a jugar deberás hacer dos sencillos pasos antes:')
print('     👉 Introducir un número entero indicando el número máximo de turnos con el que quieres jugar.')
print('')
print('     👉 Elegir con que clave secreta jugar:')
print('         ✴ Podrás elegir la clave secreta tú mismo')
print('         ✴ Para jugar de verdad y desafiar a MasterMind, introduce la palabra "nocombiCode" o simplemente dale al INTRO.')
print()
sleep(5)
print('Tienes seis posibles colores para hacer combinaciones. Las puedes escribir de estas formas:')
print('          💔  Rojo:      r  R  ')
print('          💚  Verde:     g  G  ')
print('          💙  Azul:      b  B  ')
print('          💛  Amarillo:  y  Y  ')
print('          🖤  Negro:     k  K  ')
print('          🤍  Blanco:    w  W  ')
print('')
sleep(4)
print('Dicho todo esto, ¡es hora de empezar a jugar 🎮! ¡🤞Suerte🤞!')
print('')
sleep(2)
#sleep(10)

cliente = TCPCliente(ip, port)
cliente.connect()
cliente.communication()



