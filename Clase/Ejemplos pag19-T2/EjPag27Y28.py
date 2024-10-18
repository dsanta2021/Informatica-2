class Modifiers :
    def __init__(self, name):
        self._protected_member = name #P rotected A t t ri b u t e

m = Modifiers ("SKAUL05")
print(m._protected_member )
m._protected_member = "Github" # Changing P rotected
print(m._protected_member)



class Modifiers :
    def __init__ (self , name ):
        self.__private_member = name #P riva te A t t ri b u t e

print(" O u t p u t ")
m = Modifiers ("SKAUL05")
print (m.__private_member) #comment t h i s l i n e to avoid the error
print(m._Modifiers_private_member)      #another error
m._Modifiers_private_member = "Github"
print(m._Modifiers_private_member)