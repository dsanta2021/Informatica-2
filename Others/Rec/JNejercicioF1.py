###Ejercicio F1
#count es una propiedad de String que devuelve el número de caracteres de la cadena.
#Por ejemplo, "hola".count devolvería el valor 4.
#Escribe una función que, dado un array de cadenas, devuelva otro array de enteros con las longitudes de esas cadenas.
#Es decir, dada la entrada ["pedro", "pablo", "javier"], devolvería el array [5, 5, 6].
#Intenta resolver el problema con una aproximación funcional.
#Como siempre, utiliza nombres sensatos y descriptivos para la función y para todas las variables que utilices.
def countLetters(array: list):
    long = list()
    for i in array:
        long.append(len(i))
    return long

array1 = ["pedro", "pablo", "javier"]
print(countLetters(array1))


def contarLetras(array: list):
    return list(map(lambda n: len(n), array))

print(contarLetras(array1))