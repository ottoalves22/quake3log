#importa e executa o Parser do log de Quake 3
from classes_package import parser

parser = parser.Parser()
matches = parser.parseMatch()
for x in matches:
    print(x)
    print('\n')
