# Desafio - Lógica do Jogo Super Trunfo

## 📝 Descrição

Este projeto é uma implementação em Python da lógica do clássico jogo de cartas Super Trunfo. O jogo é executado via terminal e apresenta uma batalha de cartas entre o jogador e o computador (IA). O tema das cartas é "Personagens de Anime".

Este repositório foi criado para cumprir os requisitos do desafio da disciplina, demonstrando a estruturação do código e da lógica de programação do jogo.

## 🏗️ Estrutura do Projeto

* **`jogo_super_trunfo.py`**: Arquivo principal que contém toda a lógica do jogo, incluindo a definição das cartas, as regras do jogo e a interação com o usuário.
* **`README.md`**: Documentação do projeto, explicando seu objetivo, estrutura e como executá-lo.

## ⚙️ Como Executar o Jogo

1.  Certifique-se de ter o Python 3 instalado em sua máquina.
2.  Faça o download do arquivo `jogo_super_trunfo.py`.
3.  Abra um terminal ou prompt de comando na pasta onde o arquivo foi salvo.
4.  Execute o seguinte comando:
    ```bash
    python jogo_super_trunfo.py
    ```
5.  Siga as instruções exibidas no terminal para jogar.

## 📜 Regras do Jogo (Lógica Implementada)

1.  O baralho é embaralhado e dividido igualmente entre o jogador e o computador.
2.  A cada rodada, o jogador da vez escolhe um atributo da sua carta do topo.
3.  O jogador com o maior valor no atributo escolhido vence a rodada e fica com a carta do oponente.
4.  O vencedor da rodada anterior é quem escolhe o atributo na rodada seguinte.
5.  O jogo termina quando um dos jogadores fica sem cartas. O jogador que tiver todas as cartas do baralho é o grande vencedor.
