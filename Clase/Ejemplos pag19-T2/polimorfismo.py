class Perro:
    def hablar(self):
        print("Guau, Guau!")
class Gato:
    def hablar(self):
        print("Miau, Miau!")
class Vaca:
    def hablar(self):
        print("Muuu, Muuu!")
def llama_hablar(x):
    x.hablar()

llama_hablar(Perro())
llama_hablar(Gato())
llama_hablar(Vaca())

print()

lista = [Perro(), Gato(), Vaca()]
lista[0].hablar()
lista[2].hablar()
lista[1].hablar()

print()

for i in lista:##Hace la función hablar de toda la lista (se recorre con el for)
    i.hablar()
