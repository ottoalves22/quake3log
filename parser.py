from game import game as match
from collections import defaultdict
import json
'''
x = match('1', ['Otto', 'Loga'], [['Otto', 2], ['Logan', 5]])
data = x.jsonificado()
print(data)
'''
game = 0
f = open("games.log", "r")
for x in f:
    if 'InitGame' in x:
        game += 1
    '''
    if 'killed' in x: # criar funcao para medir abates
        if '<world>' in x:
            pass #descontar 1 abate do nome que morreu para <world>
        else:
            print((x)) #contabilizar abate pro primeiro nome
'''
print(game)
