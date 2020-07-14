from game import game as match
from collections import defaultdict
import json
'''
x = match('1', ['Otto', 'Loga'], [['Otto', 2], ['Logan', 5]])
data = x.jsonificado()
print(data)
'''
def newPlayer(entrada):
    aux = entrada.split("n\\")[1].split("\\t")[0]
    return aux

game = 0
jogadores = {}

f = open("games.log", "r")
for x in f:
    if 'InitGame' in x:
        game += 1
    if 'ClientUserinfoChanged' in x:
        player = newPlayer(x)
        if player in jogadores:
            pass
        else:
            jogadores[player] = 0
    #if 'Shutdown' in x:
    #    break
    '''
    if 'killed' in x: # criar funcao para medir abates
        if '<world>' in x:
            pass #descontar 1 abate do nome que morreu para <world>
        else:
            print((x)) #contabilizar abate pro primeiro nome
'''
print(jogadores)
