import getopt
import sys
from servidorTCP import TCPservidor

def conseguirArgumentos ():
    ip = "127.0.0.1"
    port = 1234

    opts , args = getopt.getopt(sys.argv [1:] ,"i:p:", ["ip=", "port=", "nombreJugador="])
    for o, a in opts:
        if o in ("-i", "--ip"):
            ip = a
        elif o in ("-p", "--port"):
            port = a
    return ip , port

def comprobarArgumentos (ip , port):
    port_ok = True
    ip_ok = True

    try:
        port = int(port)
    except ValueError:
        port_ok = False
    if len(ip) < 7:
        ip_ok = False
    return ip_ok , port_ok


##### MAIN #####
ip, port = conseguirArgumentos()
ip_ok, port_ok = comprobarArgumentos(ip, port)

#Una forma de hacerlo
if not ip_ok:
    print('Error de ejecucución de la aplicación. Debe usar el parámetro -i o --ip = <dirección que desee>')
if not port_ok:
    print('Error de ejecucución de la aplicación. Debe usar el parámetro -p o --port = <puerto que desee usar>')
    exit(-1)

''' #Otra forma de hacerlo 
if not ip_ok or not port_ok:
    print('Los parámetros son incorrectos. Ejecute python3 argumentos.py -i IP -p Puerto')
    exit(-1)
'''

servidor = TCPservidor(ip, int(port))
servidor.crear()
servidor.comunication()

