#utiliza o parser para criar um ranking de jogadores com mais abates em uma partida
from parser import Parser
class Ranker():
    def ranking(self):
        parser = Parser()
        resultados = parser.parseMatch()
        print(resultados)

rank = Ranker()
rank.ranking()
