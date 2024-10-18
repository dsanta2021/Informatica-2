###Colecciones
#Listas
#Sets
#Diccionarios
#Estos tipos se conocen con el nombre genérico de colecciones, y su propósito es almacenar conjuntos de elementos.

#Listas
    #Las listas son secuencias de tipos homogéneos; es decir, los elementos que contienen son del mismo tipo.
    #Su característica principal es la indexación: cada elemento tiene asociado un índice de acceso directo mediante el
    # que se puede acceder a su valor.
someOddNumbers = [7, 5, 3, 1]   # list of int, initialized with some values.
aFewValues = []                 # list empty created with []
lessValues = list()             # list empty created with list()

    #Indexación:
print(someOddNumbers[0])
print(someOddNumbers[1])
print(someOddNumbers[2])
print(someOddNumbers[3])

    #Añadir elemento
someOddNumbers = someOddNumbers + [9]           # Append another array
print(someOddNumbers)
someOddNumbers.append(11)                       # Append a single element. The array is mutated.
print(someOddNumbers)

    #Recorrer lista
for i in range (len(someOddNumbers)):
    print(someOddNumbers[i])

    #Contar número de elementos que hay en una lista
print(someOddNumbers.count(8))

    #Posición del elemento x (buscar el índice del elemento x)
print(someOddNumbers.index(7))

    #Sumar listas
print(someOddNumbers + someOddNumbers)

    #Iteración
for v in someOddNumbers:
    print(v, v * 2)

print (someOddNumbers)
someOddNumbers.reverse()
for v in someOddNumbers:            #Dado la vuelta
    print(v, v * 2)

for v in sorted(someOddNumbers):    # 'sorted' -> ordenarlo
    print(v, v * 2)


#Diccionarios
'''
Los diccionarios son un conjunto de parejas nombre y valor.
El nombre es usualmente un String, pero no tiene por qué.
Por este motivo se le llama generalmente clave en lugar de nombre.
Los diccionarios se utilizan muchísimo para relacionar datos entre sí.
Por ejemplo, en una aplicación de contactos, la clave podría ser el nombre de la persona y el valor su número de teléfono.
Un sistema de DNS podría implementarse también con un gran diccionario: a cada nombre de servidor se le asocia su dirección IP.
'''
#Para crear un diccionario vacío podemos usar varios métodos
dns = {}
other_dns = dict ()
print (type(dns), type(other_dns))

    #Ej:
dns["www.urjc.es"] = "212.128.240.50"
dns["google.com"] = "172.217.17.14"
dns["stanford.edu"] = "171.67.215.200"
print(dns["google.com"])

    #Ej
ages = {"Manuel":30}    # Forma de definir el primer elemento de un diccionario
ages["Pablo"] = 25
ages["Javier"] = 20
print (ages)

#Iteración:
def printDnsDictionary(dns):
    for key, value in dns.items():
        print(f"{key} => {value}")
        # print(key,'-->', value)

printDnsDictionary(dns)

'''
Las operaciones básicas en diccionarios son:
    - Añadir pares clave-valor. Se modifican los valores anteriores en caso de repetición de la clave.
    - Consultar el valor asociado a una clave.
    - Eliminar elementos, que veremos a continuación.
'''

#Eliminar elemento
dns.pop("google.com")

printDnsDictionary(dns)

#Podemos, incluso, asociar "varios" valores usando tuplas u otros tipos agregados.
contacts = {}

contacts["Pablo"] = [25, "pablo@xxxxx.com"]
contacts["Javier"] = [20, "javier@yyyyy.com"]

for (name, (age, email)) in contacts.items():
    print(f"{name} is {age} years old and can be contacted at {email}.")

'''
Para poder iterar todos los elementos del dicionario, se debe llamar a la función items() que permite acceder a la vista 
de todas las claves con sus valores asociados.
También existen otras dos vistas:
    - keys() que devuelve la vista de todas las claves del diccionario.
    - values() que devuelve las vistas de los valores contenidos en el diccionario.
'''


#Sets
'''
Los sets o conjuntos son, como los arrays, secuencias homogéneas de valores. Se diferencian de ellos en:
    - No pueden contener elementos repetidos.
    - No existe un índice de posición asociado a cada elemento. Si iteramos un Set podemos obtener valores en cualquier orden.
Los sets se utilizan mucho menos que los arrays, pero son muy útiles cuando queremos garantizar que los elementos sean únicos.
'''

    #Ej: buscar duplicados
def findDuplicates(names):
    uniqueNames = set()
    duplicates = set()
    for name in names:
        if name in uniqueNames:
            duplicates.add(name)
        else:
            uniqueNames.add(name)
    return duplicates

print(findDuplicates(["pedro", "ana", "javier", "ana", "ana", "pablo", "pablo"]))


