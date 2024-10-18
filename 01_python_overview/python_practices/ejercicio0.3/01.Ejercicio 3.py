# Escribe aquí tu código
def gcd(x, y):
    # condición de parada:
    # se va restando la varibale con menos valor al la de mayor valor hasta que una de las dos sea 0.
    # El mcd es el valor de la variable diferente de 0.
    if x==0 and y!=0:
        return y
    if x>=y:
        x= x-y
    if y==0 and x!=0:
        return x
    if y>=x:
        y= y-x
    #llamada recursiva
    return gcd(x, y)

#casos de prueba
print(gcd(270,192)) # 6

print(gcd(9, 6)) # 3

print(gcd(30, 75)) # 15

