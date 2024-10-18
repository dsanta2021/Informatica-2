#Ejercicio 0.1 --> Calcular si un año es bisieto

#Datos:
#Un año es bisiesto si:
# 1) El año es divisible entre 4 y no entre 100.
# 2) El año es divisible entre 100 y 400. Es decir: No serán años bisiestos los que sean múltiplos de 100, excepto si también lo son de 400.
# Dicho esto podemos definir tres sucesos:
#     A) Múltiplo de 4.
#     B) Múltiplo de 100.
#     C) Múltiplo de 400.
# Con ellos podemos crear una función lógica: (A ∩ ¬B) ∪ (B ∩ C). Que haciendo la reducción por los mapas de Karnaugh es lo mismo que: (A ∩ ¬B) ∪ C.
# Es decir, un año es bisiesto si es múltiplo de 4 y no de 100 o si es múltiplo de 400.

#Código:
def calcularBisiesto (year: int):   #Esta función funciona para que se cumplan los datos.
    if (year%4==0 and not year%100==0) or (year%400==0):  #Implementación de la función lógica.
        print('El año', year,'SI es bisiesto (tiene 366 días).')   #Si se cumple la condición anterior, el año si es bisiesto
    else:
        print('El año',year,'NO es bisiesto (tiene 365 días).')    #En el caso contrario, es decir, cuando no se cumple la condición, el año no es bisiesto.

#calcularBisiesto(2022)
#calcularBisiesto(2021)
#calcularBisiesto(2019)
#calcularBisiesto(400)
#calcularBisiesto(1000)
#calcularBisiesto(4000)
#calcularBisiesto(12)

yearEscrito = int(input('Escriba un año: '))  #Pide un año por pantalla y lo guarda en una variable.
calcularBisiesto(yearEscrito)                 #Llamada a la función utilizando el número introducido por pantalla.


#Comentarios.
#Para no escribir tantas veces la llamada de la función (por eso hay un bloque nombrado de llamdo de funciones) y que siempre sean los mismos números,
#he buscado cómo introducir un valor por pantalla y que así sea más interactivo el programa y con más opciones numéricas.
#He encontrado el comando input. Pero como los tipos no coincidían al meter un número (saltaba error), he puesto
#el comando input dentro del comando int para que el número introducido se covierta en un número entero válido para la función.