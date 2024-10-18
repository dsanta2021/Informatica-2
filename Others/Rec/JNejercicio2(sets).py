###Ejercicio 2 (Sets)
#Implementa un contador.
#Escribe una función que acepte como parámetro de entrada una lista de Strings, y devuelva como salida un diccionario
# cuyas claves serán los elementos (únicos) de la lista, y cuyos valores serán el número de veces que se repiten en la lista.
def countElements(array: list) -> dict:
    diccionary = dict()
    long = len(array)
    for i in range(long):
        if array[i] in diccionary.keys():
            diccionary[array[i]] = diccionary[array[i]] + 1
        else:
            diccionary[array[i]] = 1
    return diccionary

print(countElements(["pedro", "ana", "javier", "ana", "ana", "pablo", "pablo"]))


def countNames(names):
    counter = dict()
    for name in names:
        if name in counter.keys():
            counter[name] = counter[name] + 1
        else:
            counter[name] = 1
    return counter

print(countNames(["pedro", "ana", "javier", "ana", "ana", "pablo", "pablo"]))
