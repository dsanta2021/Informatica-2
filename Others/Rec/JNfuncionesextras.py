###Funciones Extras
#split
'''
    Que sirve para trocear cadenas utilizando un carácter específico como separador o token.
        csv = "David;Jesús;Javier"
        x = csv.split(";")
        print(x)

    El resultado de hacer split utilizando ";" como separador en la cadena csv es una lista con los nombres:
        ['David', 'Jesús', 'Javier']
'''
    #Ejemplo
names = 'David¬Adam¬Lidia'
separado = names.split('¬')
print(separado)


#slicing
'''
    Consiste en seleccionar un trozo de la cadena desde una posición determinada de inicio y fin.
       Probar el siguiente fragmento para ver como seleccionar los caracteres de 2 a 5 de la cadena "Hello, World!"

        b = "Hello, World!"
        a = b[2:5]
        print( "Hey "  +  a )
'''
    #Ejemplo
b = 'Hola, David'
a = b[6:11]
print('Hey ' + a)