###Ejercicio 1
#Escribe una función que calcule el cuadrado de un número entero.
#Debe cumplir:
    #Su nombre debe ser square.
    #Debe aceptar un único argumento llamado number, de tipo Int.
    #Debe devolver un Int, que será el cuadrado del número suministrado.
def square(number: int) -> int:
    return number**2

cuadrado2 = square(2)
print(cuadrado2)
print(square(8))
n = 50
print(square(n))
