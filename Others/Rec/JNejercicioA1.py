###Ejercicio A1
#Escribe una función que reciba como parámetro un array de números enteros, y devuelva la suma de los mismos.
def sumaArray(array: list):
    resultado = 0
    for i in range(len(array)):
        resultado = resultado + array[i]
    return resultado

array1 = [1, 2, 3, 4]
print(sumaArray(array1))

array2 = [-1, 15, -3, 6]
print(sumaArray(array2))

array3 = [-1, 0, 1]
print(sumaArray(array3))
