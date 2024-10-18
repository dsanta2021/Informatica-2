#Ejercicio1

def readTopPlayers():  # Función examen
    mmTopPlayers = {}
    f = open("topMMPlayers.txt", "rt")
    data = f.read()
    players = data.split("#")
    print(players)

    for player in players:
        match = player.split("-")
        print(match)
        mmTopPlayers[match[0]] = match[1]

    f.close()
    return mmTopPlayers

prueba1 = readTopPlayers()
print(prueba1)

