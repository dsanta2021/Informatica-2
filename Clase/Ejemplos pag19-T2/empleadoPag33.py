class Empleado:
# I n i c i a l i z a n d o
    def __init__ (self):
        print('Empleado creado.')
# Eliminando ( llamando d e s t r u c t o r )
    def __del__ (self):
        print('Destructor llamado , Empleado eliminado .')

obj = Empleado ()
print('Todavía estamos en el MAIN')
print('Seguimos...')