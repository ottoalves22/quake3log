from parser.parser import Parser

parser = Parser()
matches = parser.parseMatch()
for x in matches:
    print(x)
    print('\n')
