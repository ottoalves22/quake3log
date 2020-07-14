#classe com funções que contabilizam abates
class Score():
    def newPlayer(entrada, jogadores): #adiciona um novo jogador que se logou ao conjunto de jogadores da partida
        aux = entrada.split("n\\")[1].split("\\t")[0]
        if aux in jogadores:
            return jogadores
        else:
            jogadores[aux] = 0
            return jogadores

    def killed(entrada, jogadores):
        if '<world>' in entrada: #desconta um abate do jogar morto pelo ambiente caso suas Kills > 0
            morto = entrada.split("killed ")[1].split(" by")[0]
            if jogadores[morto] > 0: jogadores[morto] -= 1
            return jogadores
        else:
            matador = entrada.split(": ")[2].split(" killed ")[0]
            jogadores[matador] += 1
            return jogadores

    def finalScore(jogadores): #contabiliza abates de cada jogador
        aux = 0
        for key in jogadores:
            aux += jogadores[key]
        return aux

    def playersList(jogadores): #lista jogadores da partida
        aux = []
        for key in jogadores:
            aux.append(key)
        return aux
