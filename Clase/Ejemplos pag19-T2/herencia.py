import math



class punto:
    __y: float = 0.0
    __x: float = 0.0

    def __init__(self, a, b):
        self.__x = a
        self.__y = b

    def moverA(self, newX, newY):
        x = newX
        y = newY

    def distancia(self, P):
        return (math.sqrt((self.__x - P.getX()) ** 2 + \
                          + (self.__y - P.getY()) ** 2))
    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def mostrar(self):
        print (self.__x, self.__y)

class poligono:
    __vertices = []

    def __init__(self, listVertices):
        self.__vertices = listVertices

    def perimetro(self):
        pass
    # Calculo del perimetro sumando las distancias

    def mostrar(self):
	    for i in self.__vertices:
            i.mostrar()
    # mostrar la info del poligono

    def area(self):
        pass
# Calcular el area del poligono

class rectangulo(poligono):
    #nuevas caracteristicas de la sublcase
    def __init__(self, orig:punto, b:float, h:float,\
                 vertices:list):
        super().__init__(vertices) ##inicializo el constructor con lo que se ha heredado.
        self.__origen = orig
        self.__base = b
        self.__altura = h

    def perimetro(self):
        return (self.__base+self.__altura)*2

    def mostar (self):
        print ("Base y altura:"self.__base, self.__altura)
        self.__origen.mostrar()
        super().mostrar() ##Llamo con el super al mostrar del padre

if __name__ == '__main__':
    p= punto(2.3, 3.2)
    poli= poligono([punto(3,5), punto(2,1)], punto(5,6), punto(7,8)])

    poli.mostrar()

    rect= rectangulo(p, 2.0, 5.0,  [punto(3,5), punto(2,1)], punto(5,6), punto(7,8)])
    rect.mostar()

    print.(p.getX(), p.getY())

