# quake3log
Aplicação que transforma um log de uma partida de Quake 3 em JSON com estatísticas a partir de um log.

 - Instalação: Crie um ambiente virtual, ative-o e execute o comando - pip3 install -r requirements.txt -
    As dependências do projeto podem ser conferidas no arquivo requirements.txt.

 - Execução:
     - python3 executeParser.py : Transforma o log com todas partidas para o formato seguinte
      game_1: {
        total_kills: 45;
        players: ["Dono da bola", "Isgalamido", "Zeh"]
        kills: {
          "Dono da bola": 5,
          "Isgalamido": 18,
          "Zeh": 20
        }
      } 
