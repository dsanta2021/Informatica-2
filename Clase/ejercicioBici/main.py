class Bicicleta:

    def __init__(self,velocidad, plato,pinion): #las tres variables son int
        self.velocidadActual = velocidad
        self.platoActual = plato
        self.pinionActual = pinion

    def acelerar(self):  #Duplica la velocidad actual
        self.velocidadActual = self.velocidadActual*2

    def frenar(self):  #Reduce a la mitad la velocidad actual
        self.velocidadActual = self.velocidadActual/2

    def cambiarPlato(self, plato):  #Cambio de plato
        self.platoActual = plato

    def cambiarPinion(self, pinion):  #Cambio de piñón
        self.pinionActual = pinion

    def mostrarVelocidad(self): #Muestra la velocidad actual
        print ('La velocidad a la que va el ciclista es:',self.velocidadActual)

    def mostarPlaPi(self):
        print ('Utilizando el plato', self.platoActual, 'y el piñón', self.pinionActual)

#---MAIN---
print('---miBiclicleta---')
miBicicleta = Bicicleta(50,2,5)
miBicicleta.mostrarVelocidad()
miBicicleta.acelerar()
miBicicleta.mostrarVelocidad()
miBicicleta.frenar()
miBicicleta.mostrarVelocidad()
miBicicleta.mostarPlaPi()
print()
print('---tuBiclicleta---')
tuBicicleta = Bicicleta(35,1,3)
tuBicicleta.mostrarVelocidad()
tuBicicleta.acelerar()
tuBicicleta.mostrarVelocidad()
tuBicicleta.frenar()
tuBicicleta.mostrarVelocidad()
tuBicicleta.mostarPlaPi()
