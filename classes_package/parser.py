from .game import Game as match
from .score import Score as score
from collections import defaultdict
import json
import os

diretorio = os.path.dirname(os.path.abspath(__file__))
log = os.path.join(diretorio, 'games.log')

class Parser():
        def parseMatch(self): #funcao que exibe informações de morte de todos jogos no log e retorna uma lista com as mesmas
            game = 0 #numero da partida
            abateswrld = 0 #mortes por ambiente
            jogadores = {} #jogadores e pontos
            allMatches = [] #lista com informações de cada partida

            f = open(log, "r")
            for x in f:
                if 'InitGame' in x:
                    game += 1
                if 'ClientUserinfoChanged' in x:
                    jogadores = score.newPlayer(x, jogadores)
                if 'killed' in x: # criar funcao para medir abates
                    if '<world>' in x: abateswrld += 1
                    jogadores = score.killed(x, jogadores)
                if 'Shutdown' in x: #partida finalizada, hora de criar estatisticas e esvaziar dict de jogadores e abates
                    abateswrld += score.finalScore(jogadores)
                    listaJogadores = score.playersList(jogadores)
                    partida = match('game_'+str(game), listaJogadores, jogadores, abateswrld)
                    abateswrld = 0
                    jogadores = {}
                    resultados = partida.jsonificado()
                    allMatches.append(resultados)
            return allMatches
