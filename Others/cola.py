# Creamos la clase node
class nodo:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# Creamos la clase cola
class cola:
    def __init__(self):
        self.raiz = None
        self.fondo = None
        self.tamanio = 0

    #Método que devuelve si la cola está vacía
    def vacio(self):
        return self.raiz == None

    # Método que devuelve el primer elemento de la cola
    def frente(self):
        return self.raiz

    # Método que devuelve el último elemento de la cola
    def final(self):
        return self.fondo

    # Método para agregar elementos en el frente de la cola
    def encolar(self, data):
        nuevoNodo = nodo(data=data, next=None)
        if self.vacio():
            self.raiz =nuevoNodo
            self.fondo = nuevoNodo
        else:
            self.fondo.next = nuevoNodo
            self.fondo = nuevoNodo
        self.tamanio +=1

    # Método para verificar si la estructura de datos esta vacía
    def extraer(self):
        if not self.vacio():
            informacion = self.raiz.data
            if self.raiz == self.fondo:
                self.raiz = None
                self.fondo = None
            else:
                self.raiz = self.raiz.next
            return informacion
        else:
            return None


    # Método para imprimir la cola de nodos
    def mostrar(self):
        node = self.raiz
        while node != None:
            print(node.data, end=" => ")
            node = node.next
        print()



    def buscar(self, key):
        curr = self.raiz
        while curr and curr.data != key:
            curr = curr.next
        if curr:
            return True
        else:
            return False




c = cola()  # Instancia de la clase
c.encolar(5)
c.encolar(7)
c.encolar(9)
c.encolar(10)
c.mostrar()  # Imprimimos la lista de nodos
c.extraer()
c.mostrar()
print (c.buscar(5))

