from flask import Flask, jsonify, request
from .classes_package import parser

app = Flask(__name__)

def matches():
    parseador = parser.Parser()
    matches = parseador.parseMatch()
    return matches


@app.route('/', methods=["GET"])
def allMatches():
    res = matches()
    return jsonify(res)


@app.route('/findmatch', methods=["GET"])
def matchResults():
    res = matches()
    id = request.args.get('id')
    result = {}
    for x in res:
        for key in x:
            if key == id:
                result = x
                return jsonify(result)
    return('Nenhum jogo encontrado')
