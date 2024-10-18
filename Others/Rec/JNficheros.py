###Ficheros
#Abrir fichero
    #La función principal para trabajar con ficheros es open().
    #Necesitamos pasarle dos parámetros:
    #El nombre del fichero que queremos manipular.
    #Y el modo en el que lo queremos manipular.
    #Hay cuatro modos diferentes de abrir un fichero.
        #"r" - Read. Es el valor por defecto. Abre el fichero para leer, y nos dará error si el fichero no existe.
        #"a" - Append. Abre el fichero para añadir datos, lo crea si no existe.
        #"w" - Write. Abre el fichero para escribir, crea el fichero si no existe.
        #"x" - Create. Crea el fichero especificado, y nos dará un error si el fichero ya existe.
    #Y además, podemos especificar si lo trataremos como binario o como texto.
        #"t" - Text. El modo texto es el valor por defecto.
        #"b" - Binary. Es el modo binario (por ejemplo imágenes).

    #Ejemplos:
'''
f = open('fichero.txt', 'rt')           · Abre el fichero en forma de texto y en lectura

f = open('fichero.txt', 'at')           · Abre el fichero o lo crea en forma de texto para añadir datos

f = open('fichero.txt', 'wt')           · Abre o crea el fichero en forma de texto para escibir

f = open('fichero.txt', 'xt')           . Crea un fichero en modo texto
'''
import os

#Cerrar fichero
    #close() cierra la conexión que hemos abierto para manipular el fichero.
    #Es una buena práctica cerrar el fichero cuando hemos terminado.

    #Ejemplo:
'''
f = open('fichero.txt', 'at')
f.close         · Cierra el fichero abierto
'''


#Lectura de ficheros
    #Ejemplo:
file = open('ejemploFicheros.txt', 'at')
file.write('Hola, bienvenido a ejemploFicheros.txt')
file.write('. Este es un fichero para hacer pruebas.')
file.close()
file = open('ejemploFicheros.txt', 'rt')
print(file.read())
file.close()


#Borrar fichero
    #Utilizar la libreria os (import os)
    #Ejemplo:
os.remove('ejemploFicheros.txt')
