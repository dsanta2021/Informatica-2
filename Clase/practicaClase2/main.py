class VendedorAutos:
    __ventasRealizadas: int = 0
    def __init__ (self, nombre_id, anios):
    #nombre_id: string y anios: int
        self.nombre = nombre_id
        self.edad = anios

    def venderCoche(self):
        self.__ventasRealizadas += 1

    def porPantalla(self):
        print('El nombre del vendedor es:',self.nombre)
        print('El vendedor tiene',self.edad,'años y ha vendido', self.__ventasRealizadas, 'autos')


v1= VendedorAutos ('David', 25) #instancia
v2= VendedorAutos ('Pepe', 38)
#VendedorAutos.porPantalla(v1) #Funciona pero no es correcto

v1.porPantalla()
v1.venderCoche()
v1.porPantalla()

v2.porPantalla()