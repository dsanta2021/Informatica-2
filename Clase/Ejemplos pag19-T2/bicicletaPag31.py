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

class BicicletaMontana:

    def __init__(self, suspension:int):
        super().__init__()


##Ejemplo
mm = Bicicleta(100, 'mediano', 4)
mm.mostrarVelocidad()
mm.mostarPlaPi()
mm.frenar()
mm.cambiarPinion(3)
mm.mostrarVelocidad()
mm.mostarPlaPi()
