from collections import defaultdict
import json

def kill_sum(arr): #recebe como entrada uma lista de listas [[nome, abates], ...] e soma abates de todos nomes
    d = 0
    for i, j in arr:
        d += (j)
    return d

class game(): #classe que gera um json com informações da partida
    def __init__(self, nameEntry, playersEntry, killsEntry):
        self.name = nameEntry
        self.total_kills =  kill_sum(killsEntry)#sumatorio de kills
        self.players = playersEntry #lista ['Otto', 'Loga']
        self.kills = killsEntry #lista de lista [['Otto', 2], ['Logan', 5]]

    def jsonificado(self):
        data = {
            self.name: {
                'total_kills': self.total_kills,
                'players': self.players,
                'kills': {}
            }
        }
        d = defaultdict(list)
        d = dict(d)
        for i, j in self.kills:
            d[i] = j

        data[self.name]['kills'] = d
        return data
