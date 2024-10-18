from MasterMind02 import MasterMindGame

mm = MasterMindGame('GRRG')

print('secretCode', mm.secretCode)

mmCombi = mm.toMasterMindColorCombination('krrk')

print('mmCombi', mmCombi)

# #Formas de saber el número de aciertos:
# #1º
# compResult = list(map(lambda x, y: x==y, mmCombi, mm.secretCode))
# print('compResult', compResult)
# cmatches = len(list(filter(lambda x: x is True, compResult)))
# print('cmatches:', cmatches)
#
# #2º
# i = 0
# match = 0
# for mmc in mmCombi:
#     if mmc == mm.secretCode[i]:
#         match = match + 1
#     i= i + 1
#print('Número de aciertos:',match)


mm.countExactMatches(mmCombi)