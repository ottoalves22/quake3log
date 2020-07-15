from classes_package import parser

def ranking(): #cria rankings por partida e ranking geral (de todas essas partidas) para cada Jogador considerando abates
    jogadores = []
    parseador = parser.Parser()
    matches = parseador.parseMatch()
    print('Ranking por partida')
    for i in matches:
        for key in i:
            name = key
            sortedMatches = {i: j for i, j in sorted(i[name]['kills'].items(), key=lambda x:x[1], reverse=True)}
            print(name)
            print(sortedMatches)
            print('\n')

ranking()
