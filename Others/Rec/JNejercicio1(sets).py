###Ejercicio 1 (Sets)
#Escribe una función que acepte como parámetro de entrada una lista de Strings, y devuelva los nombres únicos que
# figuran en la lista, sin ningún orden en particular.
#Escribe el código necesario para comprobar que funciona correctamente.
#Utiliza nombres sensatos para la función y las variables que utilices.
def nombresNoRepes(names: list):
    unicos = set()
    repetidos = set()
    long = len(names)
    for i in range(long):
        if names[i] in unicos:
            repetidos.add(names[i])
        else:
            unicos.add(names[i])
    return unicos

print(nombresNoRepes(["pedro", "ana", "javier", "ana", "ana", "pablo", "pablo"]))

def nombresNoRepes2(names: list): #Set directamente solo tiene elementos no repetidos, así que se puede hacer un set de un array directamente
    unicos = set(names)
    return unicos

print(nombresNoRepes2(["pedro", "ana", "javier", "ana", "ana", "pablo", "pablo"]))