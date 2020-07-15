from classes_package import parser

def ranking(): #retornará informações para demais executáveis
    parseador = parser.Parser()
    matches = parseador.parseMatch()
    print('Ranking por partida')
    for i in matches:
        for key in i:
            name = key
            #print(i[name]['kills'])
            sortedMatches = {i: j for i, j in sorted(i[name]['kills'].items(), key=lambda x:x[1], reverse=True)}
            print(name)
            print(sortedMatches)
            print('\n')

        #aux = i
        #name = 'game_' + str(aux)
        #print(i[name]['kills'])

ranking()
