###Ejercicio F2
#Escribe una función, usando map, para convertir un array de enteros en un array de cadenas que representen los mismos numeros.
def intToString(arrayInt: list):
    return list(map(lambda n: str(n), arrayInt))

array1 = [1, -7, 0, 55]
print(intToString(array1))


def numbersToSrings(arrayNumbers: list):
    result = list()
    for i in arrayNumbers:
        result.append(str(i))
    return result

print(numbersToSrings(array1))