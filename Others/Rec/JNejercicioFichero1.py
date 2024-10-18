###Ejercicio Fichero1
#Crea un fichero demofilex.txt.
#Escribe la siguiente frase "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
#Y lee los primeros 5 caracteres.
#No olvides cerrar el fichero al terminar.
import os

fich = open('demofilex.txt', 'wt')
fich.write("Lorem Ipsum is simply dummy text of the printing and typesetting industry.")
fich.close()

file = open('demofilex.txt', 'rt')
print(file.read(5))
file.close()

os.remove('demofilex.txt')