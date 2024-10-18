###Tuplas
#Las funciones, técnicamente, sólo pueden devolver un único valor.
#Sin embargo, en Python existe el tipo "tupla" que representa una secuencia de valores.
#Es válido que una función devuelva una tupla, que no es más que una lista de tipos entre paréntesis.
def miniDataBase():
    return ('David', 21)

person = miniDataBase()
print(person)

#Para acceder a algún elemento de la tupla:
name = person[0]
age = person[1]
print('Nombre: ', name)
print('Edad: ', age)