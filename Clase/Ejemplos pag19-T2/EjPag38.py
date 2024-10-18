class Usuario:
    def __init__(self , nombre ):
        self.__nombre_usuario = nombre

    def __str__(self):
        return self.__nombre_usuario

objetoEjemplo = Usuario ("David")
print (objetoEjemplo)
#print (objetoEjemplo.__nombre_usuario )