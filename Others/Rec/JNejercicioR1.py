###Ejercicio R1
#Escribe una funcion recursiva para calcular el factorial de un numero entero. Sabemos que:
#El factorial de 1 es 1.
#El factorial de n es el factorial de n-1.
def factorial(number: int):
    total = 1
    while True:
        if (number == 1 or number == 0) and total == 1:
            total = 1
            break
        if number == 1:
            break
        else:
            total = total * number
            number = number - 1
    return total

print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))
print(factorial(6))
print(factorial(7))
print(factorial(8))
print(factorial(9))
print(factorial(10))

def fact(n: int):
    if n <= 1:
        return 1
    return n * fact(n - 1)

print(fact(0))
print(fact(1))
print(fact(2))
print(fact(3))
print(fact(4))
print(fact(5))
print(fact(6))
print(fact(7))
print(fact(8))
print(fact(9))
print(fact(10))