###Ejercicio 2
#Escribe una función para calcular si un año es bisiesto, es decir tiene un día más 366 (29 de Febrero).
#La que vamos a escribir función debe cumplir la siguiente especificación:
    #Si el año es uniformemente divisible por 4.
    #Si el año es uniformemente divisible por 100.
    #Si el año es uniformemente divisible por 400.
    #El año es un año bisiesto (tiene 366 días).
    #El año no es un año bisiesto (tiene 365 días).
def anoBisiesto(year: int):
    if (year%4==0 and not year%100==0) or (year%400==0):
        return 'El año ' + str(year) + ' es bisiesto'
    else:
        return str(year) + ' no es un año bisiesto'


print(anoBisiesto(2020))
print(anoBisiesto(2002))
print(anoBisiesto(2022))