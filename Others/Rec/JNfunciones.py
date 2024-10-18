###Funciones
#Función sin parámetros de entrada
def hola():
    print('Hola. Esto es la función más simple')

hola()

#Función con parámetro de entrada
def escribirParametro(name: str):
    print('Bienvenido,', name)

escribirParametro('David')

#Función con varios parámetros de entrada (inicializados por defecto)
def writeParameters(name = 'David', day = 'Miércoles', number = 7):
    print('Hola,' ,name, '. Hoy es día', number, ', que es ', day)

writeParameters()
writeParameters('Adam', 'Viernes', 9)

#Función que devuelve un valor
#Es muy habitual que las funciones devuelvan valores.
#Normalmente usando la palabra reservada return la función devolvería los valores.
#Además se puede definir qué tipos se van a devolver, para esto se expresa con la "flecha" ->
def devuelveValor(name: str = 'David', day:str = 'Monday') -> str:
    return 'Hello, ' + name + ' today is ' + day

print(devuelveValor())
print(devuelveValor('Adam', 'Sunday'))
escribe = devuelveValor('Dani', 'Saturday')
print(escribe)

#Funciones Anidadas
    #Las funciones pueden anidarse dentro de otras funciones.
    #Una función anidada sólo es visible desde dentro de la función donde se encuentra.
    #Las funciones también son tipos de primer orden (es decir, tipos como cualquier otro).
    #Esto significa que una función puede aceptar como argumento o devolver otra función.
def makeIncrementer() -> int:
    def addOne(n: int) -> int:
        return n + 1
    return addOne

incrementer = makeIncrementer()
print(incrementer(41))


def makeAdder(base):
    x = 7
    def add(n):
        return base + n
    return add

adder = makeAdder(5)
print(adder(2))
print(adder(5))
decrementer = makeAdder(-1)
print(decrementer(2))
print(decrementer(5))



