#importa e executa o Parser do log de Quake 3
from classes_package import parser

def matches(): #retornará informações para demais executáveis
    parseador = parser.Parser()
    matches = parseador.parseMatch()
    return matches

partidas = matches()
for x in partidas:
    print(x)
    print('\n')
