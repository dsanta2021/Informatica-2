###Ejercicio A2
#Escribe una función que reciba como parámetro un array de números enteros, y devuelva su media como un float.
def mediaArray(array: list):
    result = 0
    long = len(array)
    for i in range(long):
        result = result + array[i]
    return result/long

array1 = [1, 2, 3, 4]
print(mediaArray(array1))

array2 = [-1, 15, -3, 6]
print(mediaArray(array2))

array3 = [-1, 0, 1]
print(mediaArray(array3))