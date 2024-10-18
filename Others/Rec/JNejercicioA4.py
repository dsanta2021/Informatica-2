###Ejercicio A4
#Escribe una función que reciba como parámetro un array de números enteros, y devuelva el elemento que tiene el valor mínimo.
def myMin(arrayInt: list):
    mini = 9999999999999
    long = len(arrayInt)
    for i in range(long):
        if mini > arrayInt[i]:
            mini = arrayInt[i]
    return mini

array1 = [0, 1, 2, 3, 4]
print(myMin(array1))

array2 = [-9, 45, 8, -72, 100, 12, -36]
print(myMin(array2))

print(myMin([6, 0, -7, 1, 9, 2]))
print(min([6, 0, -7, 1, 9, 2]))             #La palabra reservada 'min' calcula el valor mínimo