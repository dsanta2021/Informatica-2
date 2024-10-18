from MasterMind02 import MasterMindGame

MM = MasterMindGame()

print(MM.MasterMindColor("K"), "Correcto. El color de la bola es negro.")

print(MM.MasterMindColor("💚"), "Correcto. El color de la bola es verde.")

print(MM.toMasterMindColorCombination("rgbk"), "Correcto. Con la combinación 'rgbk' obtenemos las lista: " + str(['💔', '💚', '💙', '🖤']))

print(MM.toMasterMindColorCombination("R💚gk"), "Correcto. Con la combinación 'R💚gk' obtenemos las lista: " + str(['💔', '💚', '💚', '🖤']))

try:
    print(MM.toMasterMindColorCombination("kskej"))
except:
    print("Correcto. Error tratando de convertir a colores MasterMind la combinación 'kskej' no válida.")

print(MM.randomCode(4), "Correcto. Obtenemos un diccionario de 4 colores aleatorios.")
print(MM.randomCode(2), "Correcto. Obtenemos un diccionario de 2 colores aleatorios.")
print(MM.randomCode(9), "Correcto. Obtenemos un diccionario de 9 colores aleatorios.")

# combinación de cuatro colores por defecto
testGame = MasterMindGame()

print(testGame.secretCode, "Correcto. Al inicializar la clase testGame por defecto genera una clave aleatoria de cuatro colores.")

# combinación de cuatro colores específica
testGame = MasterMindGame("RGBK")

if testGame.secretCode != ['💔', '💚', '💙', '🖤']:
    print("Error al crear una partida con una combinación concreta.")
else:
    print("Correcto. Ha generado la clave secreta: " + str(['💔', '💚', '💙', '🖤']) + " con la combinación que hemos pedido RGBK.")

# combinaciones de cuatro colores aleatorias
gamesAreAllTheSame = True

for g in range(5):
    game1 = MasterMindGame()
    game2 = MasterMindGame()
    if game1.secretCode != game2.secretCode:
        gamesAreAllTheSame = False

if gamesAreAllTheSame:
    print("Parece que `randomCode` está generando siempre la misma clave.")
else:
    print("Correcto. Genera combinaciones diferentes de claves de tiradas diferentes.")

# genera una clave válida aunque le pasemos una cade inválida
anotherGame = MasterMindGame("esta cadena no es válida")

if len(anotherGame.secretCode) != 4:
    print("La clave aleatoria debe tener 4 colores")
else:
    print("Correcto. Ha generado una clave aleatoria de cuatro colores aunque le hemos pasado una clave inválida.")
