from MasterMind03 import MasterMindGame

mm = MasterMindGame('RGGB')
mm2 = MasterMindGame('bygw')

#************** TEST-0 **********************
print("Test 0 - Comprobamos que el Secret Code es el que hemos fijado.")
print("Secret code", mm.secretCode)
print('')
#************** TEST-1 **********************
print("Test 1 - Comprobamos si es una combinación MasterMind Colors correcta")
mm.newTurn("rdsa")
print('')
#************** TEST-2 **********************
print("Test 2 - Comprobamos si es correcta la longitud de la combinación: ")
mm.newTurn("rbkywg")
print('')
#************** TEST-3 **********************
print("Test 3 - Comenzamos a jugar (SI se acierta la combinación)")
mm.newTurn("RRGG") #Combinación correcta -> enseña la combinación metida, el número de aciertos y semiaciertos.
print('')
mm.newTurn("💔💔💔💔💔💔💔") #Combinación no correcta -> mensaje: "Debe hacer una combinación de 4 colores. Por favor, pruebe de nuevo.".
print('')
mm.newTurn("BBKK")
print('')
mm.newTurn("RYYR")
print('')
mm.newTurn("RGGB") #A partir de este punto, el juego "ha cabado" ya que se ha acertado la combinación correcta.
print('')          #Entonces, por mucho que se siga poniendo combinaciones, se mostrará el mensaje de que el juego ha finalizado.
mm.newTurn("RGGB")
print('')
mm.newTurn("RGGB")
print('')
mm.newTurn("RGGB")
print('')
mm.newTurn("RGGB")
print('')
mm.newTurn("RGGB")
print('')
mm.newTurn("RGGB")
print('')
mm.newTurn("RGGB")
print('')
mm.newTurn("RGGB")
print('')
mm.newTurn("RGGB")
print('')
mm.newTurn("RGGB")
print('')
mm.newTurn("RGGB")
print('')
#************** TEST-4 **********************
print("Test 4 - Otra partida (NO se acierta la combinación)")
mm2.newTurn("kkyb")
print('')
mm2.newTurn("💔💔💔💔💔💔💔") #Escribe:"Debe hacer una combinación de 4 colores. Por favor, pruebe de nuevo.", por tener una combinación con una longitud mayor de la permitida (4).
print('')
mm2.newTurn("💚💙🖤💔")
print('')
mm2.newTurn("yrry")
print('')
mm2.newTurn("wggb")
print('')
mm2.newTurn("➰#¬|")#Escribe:"Combinación incorrecta. Por favor, pruebe de nuevo", por no tener en la combinación colores válidos
print('')
mm2.newTurn("RjGB") #Escribe:"Combinación incorrecta. Por favor, pruebe de nuevo", por no tener en la combinación colores válidos
print('')
mm2.newTurn("bbbb")
print('')
mm2.newTurn("rybk")
print('')
mm2.newTurn("yybb")
print('')
mm2.newTurn("wwww")
print('')
mm2.newTurn("bwwb")
print('')
mm2.newTurn("wkkk")
print('')
mm2.newTurn("ybky")
print('')
mm2.newTurn("wryk")
print('')







