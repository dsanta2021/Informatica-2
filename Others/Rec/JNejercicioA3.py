###Ejercicio A3
#Escribe una función que reciba como parámetro un array de números enteros, y devuelva el elemento que tiene el valor máximo.
#Nota: posiblemente tengas que usar if para comparar valores.
#Su funcionamiento es muy parecido al de otros lenguajes de programación.
#Nota: llama a la función myMax, porque max ya está definido en Python.
def myMax(arrayInt: list):
    maxi = 0
    long = len(arrayInt)
    for i in range(long):
        if maxi <= arrayInt[i]:
            maxi = arrayInt[i]
    return maxi

array1 = [0, 1, 2, 3, 4]
print(myMax(array1))

array2 = [12, -5, 8, -45, 36, 7, -1]
print(myMax(array2))

print(myMax([6, 0, -7, 1, 9, 2]))
print(max([6, 0, -7, 1, 9, 2]))         #La palabra reservada 'max' calcula el máximo