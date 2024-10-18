###Variables
a = 5                                   #Int --> Entero
b = 7.63                                #Float --> Real
c = 'Repasando para la recuperación'    #String --> Cadena de caracteres

print(type(a))
print(type(b))
print(type(c))

#Conversión automática
ab = a + b                               #Suma de dos tipos de variables --> Int + Float = Float

print(type(ab))
print(ab)

#Conversión explícita
aB = a + int(b)

print(type(aB))
print(aB)

#Concatenar o añadir elementos a un conjunto con +
solution = 'El resultado es '
solution = solution + str(a)

print(solution)

#

