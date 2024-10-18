from MMClass import MasterMindGame
# Creamos la clase node
class node:
    def __init__(self, next=None, socket=None, address=None, playerID=None):

        self.socket = socket #<ip>
        self.address = address #<puerto>
        self.playerID = playerID #<nombre del jugador>
        self.gameID = None #<ID de partida>
        self.started = False #<para saber si una partida está empezada>
        self.next = next #<referencia al siguiente nodo>


# Creamos la clase linked_list
class dataBase:
    MMD = {} #Diccionario de las instancias MasterMind
    playersCount = 0 #Varible que asigna un gameID a cada instancia MM

    def __init__(self):
        self.head = None

    # Método para agregar elementos en el frente de la linked list
    def addFront(self, socket, address, playerID):
        self.head = node(socket=socket, address=address, playerID=playerID, next=self.head)


    # Método para eliminar nodos <<<<<<TENGO QUE AÑADIR PARA ELIMINAR LA INSTANCIA MM>>>>>>>
    def erase(self, playerID):
        curr = self.head
        prev = None
        while curr and curr.playerID != playerID:
            prev = curr
            curr = curr.next
        if prev is None:
            self.MMD[curr.gameID].clear() #Esto para borrar la instancia MM de MMD
            self.head = curr.next
        elif curr:
            self.MMD[curr.playerID].clear()  # Esto para borrar la instancia MM de MMD
            prev.next = curr.next
            curr.next = None


    #Método para encontrar un nodo concreto con el nombre del jugador
    def found(self, playerID): #devuleve la información del nodo
        point = self.head
        while point and point.playerID != playerID:
            point = point.next
        return point
        #Otra forma
        #while point != None:
        #    if point.playerID == playerID:
        #        return point
        #    point = point.next
        #return point


    #Método para crear partida usando el nombre del jugador1:
        # añade una instancia MM a MMD
        # cambia el gameID al valor de playersCount.
    def creteGame(self, playerID):
        encounter = self.found(playerID)
        self.playersCount += 1
        self.MMD[self.playersCount] = MasterMindGame()
        encounter.gameID = self.playersCount


    #Método para añadir a la partida un segundo jugador:
    def appendJ2(self, J1, J2):
        # Se busca J1 y J2
        player1 = self.found(J1)
        player2 = self.found(J2)

        # Se igual el gameID de J2 al de J1
        player2.gameID == player1.gameID

        # Se ponen a True el campo started
        player1.started == True == player2.started

        #Otra opción
        #Se busca a J1
        #Se saca la gameID de J1
        #Se cambia el started de J1 a True(indica que alguien se ha unido a su partida)
        #Se busca a J2
        #Se cambia gameID de J2 para que sea igual que el de J1
        #Se cambia el started de J2 a True(indica que se ha metido en una partida)


    #Comparador de nombre
        #Recorre la lista
        #Según si encuentra un nombre o no devuelve repeat(bool)
    def comparator(self, playerID):
        repeated = False
        follow = self.head
        while follow != None:
            if playerID == follow.playerID:
                repeated = True
                return repeated
            follow = follow.next
        return repeated


    #Enviar lista de las partidas
    def sendData(self):
        subsequent = self.head
        data = ''
        while subsequent != None:
            if not subsequent.started:
                name = subsequent.playerID
                turns = self.MMD[subsequent.gameID].maxturns
                data += '#' + name + '¬' + turns
            subsequent = subsequent.next
        return 'G' + data
