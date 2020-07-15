# quake3log
Aplicação que transforma um log de uma partida de Quake 3 em JSON com estatísticas a partir de um log.

 - Instalação: Crie um ambiente virtual, ative-o e execute o comando - pip3 install -r requirements.txt -
    As dependências do projeto podem ser conferidas no arquivo requirements.txt.

 - Execução:
    - python3 executeParser.py : Imprime o log parseado com todas partidas para o seguinte formato
      game_1: {
        total_kills: 45;
        players: ["Dono da bola", "Isgalamido", "Zeh"]
        kills: {
          "Dono da bola": 5,
          "Isgalamido": 18,
          "Zeh": 20
        }
      }

    - python3 executeRanking.py : Exibe o nome da partida e os jogadores em ordem crescente de acordo com seus abates

    - API:

    - Testes:

  - Estrutura:
     Os arquivos execute____.py agem como executáveis para as classes contidas no diretório classes_package.
      - A classe Games é um modelo para uma partida, contendo um construtor e um método que retorna um dicionário.
      - A classe Parser é responsável por pegar o arquivo .log (que se encontra no mesmo diretório) e o transcreve para o formato json indicado acima utilizando a estrutura de dados de dicionário.
      - A classe Score agrupa diversos métodos auxiliares, por exemplo o método killed() que altera a pontuação dos jogadores que mataram outro jogador ou para jogadores que morreram para o ambiente (perdendo um ponto)
