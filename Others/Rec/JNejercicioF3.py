###Ejercicio F3
#Escribe una función que obtenga los números cuadrados pares de los primeros N números positivos.
def squares(arrayInt: list):
    cuadrados = map(lambda n: n*n, arrayInt)
    return list(filter(lambda x: x%2==0, cuadrados))

array1 = list(range(1, 11))
print(squares(array1))

array2 = list(range(1,10,2))
print(array2)
print(squares(array2))
