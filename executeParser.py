#importa e executa o Parser do log de Quake 3
from classes_package import parser

def matches(): #retornará informações sobre as partidas ao ser executada
    parseador = parser.Parser()
    matches = parseador.parseMatch()
    return matches

#printa log parseado
partidas = matches()
for x in partidas:
    print(x)
    print('\n')
