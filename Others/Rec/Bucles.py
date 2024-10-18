###Bucles

#Bucle while
n = 1
while n < 10:
    print(f"El cuadrado de {n} es {n * n}")
    n = n + 1

    #repeat...until (pascal), en python es:
n = 1
while True:
    print(f"El cuadrado de {n} es {n * n}")
    n = n + 1
    if n == 10:
        break

#Rangos (bucle for)
for n in range(1,11):
    print(f"El cuadrado de {n} es {n * n}")

    #También se puede definir un valor de salto entre los extremos.
    #Imaginemos que śolo queremos sacar el cuadrado de los valores pares:
for n in range(0,11,2):
    print(f"El cuadrado de {n} es {n * n}")
