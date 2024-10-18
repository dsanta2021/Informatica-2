###Ejercicio F4
#Calcula la suma de los cuadrados de los numeros pares que contiene una lista de enteros.
#Debes combinar map, filter y reduce adecuadamente para conseguirlo.
from functools import reduce

def sumCuadradosInt(arrayInt: list):
    cuadrados = map(lambda x: x*x, arrayInt)
    cuadradosPares = list(filter(lambda n: n%2==0, cuadrados))
    return reduce(lambda x, y: x+y, cuadradosPares)

array1 = list(range(1,11))
print(sumCuadradosInt(array1))

array2 = list(range(1,10))
print(sumCuadradosInt(array2))