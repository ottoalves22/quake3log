from collections import defaultdict
import json

def kill_sum(arr): #recebe como entrada uma lista de listas [[nome, abates], ...] e soma abates de todos nomes
    d = 0
    for i, j in arr:
        d += (j)
    return d

class Game(): #classe que gera um json com informações da partida
    def __init__(self, nameEntry, playersEntry, killsEntry, kdEntry):
        self.name = nameEntry
        self.total_kills = (kdEntry)#sumatorio de kills
        self.players = playersEntry #lista ['Otto', 'Loga']
        self.kills = killsEntry #lista de lista [['Otto', 2], ['Logan', 5]]

    def jsonificado(self):
        data = {
            self.name: {
                'total_kills': self.total_kills,
                'players': self.players,
                'kills': self.kills
            }
        }
        return data
