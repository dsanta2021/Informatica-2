###Filtros y transformaciones funcionales
# map
# map es una función que recibe como argumento otra función, que aplica a cada uno de los elementos de la secuencia,
# y devuelve en un tipo map el resultado.
# Es por esto que es necesario la transformación del resultado en una list.
# Es decir map transforma de manera arbitraria los elementos con la función que le proporcionamo

# Forma Iterativa
squares = list()
for i in range(1, 10):
    squares.append(i * i)

print(squares)

# Forma funcional
cuadrados = list(map(lambda n: n * n, range(1, 10)))

print(cuadrados)

# Filter
# La función filter filtra o selecciona los elementos de una secuencia que cumplen una condición.
# Para ello, hay que pasarle como argumento una función que devuelve true si el elemento debe incluirse en el resultado,
# o false en caso contrario.

# Ejemplo: seleccionamos de una secuencia los números pares.
# El operador % calcula el módulo (~resto) de la división entera: el número es par si el resto de dividir entre 2 es 0.
print(list(filter(lambda x: x % 2 == 0, range(1, 11))))  # Escribe los números cuyo módulo sea 0(pares)
print(list(map(lambda x: x % 2, range(11))))  # Escribe el módulo de los números en el rango

# Reduce
    # Esta función transforma una secuencia en un único elemento.
    # reduce acepta dos argumentos:
    # - Una función que debe tener dos parámetros y será llamada por reduce de forma acumulativa (preservando el resultado de las llamadas anteriores).
    # - Un conjunto de valores.

    # Ejemplo: suma los 10 primeros números naturales:
from functools import reduce

print(reduce(lambda x, y: x + y, range(1, 11)))

    #De forma Iterativa:
def suma(array: list):
    total = 0
    for i in array:
        total =total + i
    return total

array1 = list(range(1, 11))
print(suma(array1))

