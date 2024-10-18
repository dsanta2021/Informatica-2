agenda = list()

class Persona:

    def __init__(self, nombre, apellidos, telefono):
        self.name = nombre
        self.surname = apellidos
        self.phone = telefono


def mostrar():
    print('Bienvenido a Agenda')
    print('Menú:')
    print('1 -> Añadir contacto')
    print('2 -> Enseñar todos los contactos')
    print('3 -> Salir de Agenda')
    accion = input('Elija un número según la acción que quiera realizar: ')

    if accion == '1':
        anadir()
    elif accion == '2':
        listar()
    elif accion == '3':
        salir()
    else:
        print('No ha introducido un número válido')
        salir()


def anadir():
    print('Introduzca nombre, apellido y teléfono del cliente.')
    name = input('Nombre: ')
    surname = input('Apellidos: ')
    phone = input('Teléfono: ')
    pp = Persona(name, surname, phone)
    #cliente = self.persona(name, surname, phone)
    agenda.append(pp)
    mostrar()


def listar():
    print('Los contactos actuales son: ')

    for client in agenda:
        print(client.name + ' ' + client.surname + ': ' + client.phone)
    salir = input('Pulse cualquier tecla para volv er al menú: ')
    if salir == '':
        mostrar()
    else:
        mostrar()

def salir():
    print('Gracias. Hasta pronto')
    exit(-1)


#######  MAIN  #######
mostrar()