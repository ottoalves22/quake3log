from game import game as match
from collections import defaultdict
import json
'''
x = match('1', ['Otto', 'Loga'], [['Otto', 2], ['Logan', 5]])
data = x.jsonificado()
print(data)
'''
def newPlayer(entrada, jogadores): #adiciona um novo jogador que se logou ao conjunto de jogadores da partida
    aux = entrada.split("n\\")[1].split("\\t")[0]
    if aux in jogadores:
        return jogadores
    else:
        jogadores[aux] = 0
        return jogadores

def killed(entrada, jogadores):
    if '<world>' in x: #desconta um abate do jogar morto pelo ambiente
        morto = entrada.split("killed ")[1].split(" by")[0]
        jogadores[morto] -= 1
        return jogadores
    else:
        matador = entrada.split(": ")[1].split(" killed")[0] #TODO PRECISO TIRAR O NOME DE QUEM ABATEU
        jogadores[matador] += 1
        return jogadores
        print((x)) #contabilizar abate pro primeiro nome

game = 0
abates = 0
jogadores = {}

f = open("games.log", "r")
for x in f:
    if 'InitGame' in x:
        game += 1
    if 'ClientUserinfoChanged' in x:
        jogadores = newPlayer(x, jogadores)

    '''
    if 'killed' in x: # criar funcao para medir abates
        abates += 1
        if '<world>' in x: #juntar abates em uma funcao
            pass #descontar 1 abate do nome que morreu para <world>
        else:
            print((x)) #contabilizar abate pro primeiro nome
    '''
    #if 'Shutdown' in x: #partida finalizada, hora de criar estatisticas e esvaziar dict de jogadores e abates
    #    break
print(jogadores)
