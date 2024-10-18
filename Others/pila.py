# Creamos la clase node
class nodo:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# Creamos la clase pila
class pila:
    def __init__(self):
        self.cima = None
        self.tamanio = 0

    # Método para apilar elementos
    def apilar(self, data):
        self.cima = nodo(data=data, next=self.cima)
        self.tamanio += 1

        # Método para verificar si la estructura de datos esta vacia

    def vacio(self):
        return self.cima == None


    #Método para devolver la cima.

    def getcima(self):
        return self.cima

    # Método para desapilar nodos
    def desapilar(self):
        curr = self.cima
        self.cima = curr.next
        self.tamanio -= 1

    def desapilaryretornar(self):
        nodo = self.cima()
        self.desapilar()
        return nodo.data

    def buscar(self, key):
        curr = self.cima
        while curr and curr.data != key:
            curr = curr.next
        if curr:
            return True
        else:
            return False


# Método para imprimir la pila de nodos
    def mostrar(self):
        node = self.cima
        while node != None:
            print(node.data, end=" => ")
            node = node.next
        print()

p = pila()  # Instancia de la clase
p.apilar(5)  # Apilamos varios nodos
p.apilar(8)
p.apilar(9)
p.mostrar()  # Imprimimos los nodos
p.desapilar() # Desapilamos el último
p.mostrar()  # Imprimimos los nodos
print (p.buscar(5)) #Buscamos un elemento

