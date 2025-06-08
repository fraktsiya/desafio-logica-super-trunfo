import random
import os
import time

# Função para limpar o console (funciona em Windows, Mac e Linux)
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Definição da classe Carta, que estrutura os dados de cada carta.
class Carta:
    def __init__(self, nome, ataque, defesa, inteligencia, poder):
        self.nome = nome
        self.atributos = {
            'Ataque': ataque,
            'Defesa': defesa,
            'Inteligência': inteligencia,
            'Poder': poder
        }

    # Representação em texto da carta para exibição.
    def __str__(self):
        return f"--- {self.nome} ---"

# Função principal que contém a lógica do jogo.
def jogar():
    # Criação do baralho com os personagens e seus atributos.
    baralho = [
        Carta("Goku", 100, 90, 70, 100),
        Carta("Vegeta", 95, 85, 80, 98),
        Carta("Naruto", 90, 80, 85, 95),
        Carta("Sasuke", 88, 82, 90, 93),
        Carta("Eren Yeager", 80, 70, 75, 85),
        Carta("Levi Ackerman", 92, 60, 95, 88),
        Carta("Saitama", 100, 100, 50, 100),
        Carta("Luffy", 93, 88, 70, 94),
        Carta("Zoro", 91, 85, 65, 90),
        Carta("All Might", 98, 95, 80, 99),
        Carta("Madara Uchiha", 96, 92, 94, 98),
        Carta("Itachi Uchiha", 85, 80, 98, 92),
        Carta("Gojo Satoru", 99, 97, 96, 100),
        Carta("Sukuna", 99, 94, 97, 100),
        Carta("Light Yagami", 50, 60, 100, 70),
        Carta("L Lawliet", 40, 70, 100, 65),
    ]

    # Lógica de embaralhar e distribuir as cartas.
    random.shuffle(baralho)
    metade = len(baralho) // 2
    mao_jogador = baralho[:metade]
    mao_computador = baralho[metade:]

    rodada = 1
    jogador_da_vez = "jogador"  # O jogador humano sempre começa.

    # Loop principal do jogo: continua enquanto ambos os jogadores tiverem cartas.
    while mao_jogador and mao_computador:
        limpar_tela()
        print(f"--- RODADA {rodada} ---")
        print(f"PLACAR: Você tem {len(mao_jogador)} cartas | Computador tem {len(mao_computador)} cartas.")
        
        if jogador_da_vez == "jogador":
            print("\nSua vez de escolher!")
        else:
            print("\nVez do computador escolher...")
        
        input("\nPressione Enter para ver sua próxima carta...")

        carta_jogador = mao_jogador[0]
        carta_computador = mao_computador[0]

        limpar_tela()
        print("Sua carta é:")
        print(carta_jogador)
        for i, (atr, val) in enumerate(carta_jogador.atributos.items(), 1):
            print(f"{i}. {atr}: {val}")

        # Lógica da escolha do atributo.
        if jogador_da_vez == "jogador":
            escolha = ""
            while escolha not in ['1', '2', '3', '4']:
                escolha = input("\nEscolha um atributo (1-4): ")
            atributo_escolhido = list(carta_jogador.atributos.keys())[int(escolha) - 1]
        else:
            # IA simples: o computador escolhe o atributo com o maior valor em sua carta.
            time.sleep(1) # Pausa para simular o pensamento do computador
            atributo_escolhido = max(carta_computador.atributos, key=carta_computador.atributos.get)
            print(f"\nO computador escolheu: {atributo_escolhido}")
            time.sleep(1)

        valor_jogador = carta_jogador.atributos[atributo_escolhido]
        valor_computador = carta_computador.atributos[atributo_escolhido]
        
        print("\n--- COMPARANDO ---")
        print(f"Atributo: {atributo_escolhido}")
        print(f"Sua carta: {carta_jogador.nome} ({valor_jogador})")
        print(f"Carta do computador: {carta_computador.nome} ({valor_computador})")
        time.sleep(2)

        # Lógica de comparação e transferência de cartas.
        if valor_jogador > valor_computador:
            print("\nVocê venceu a rodada!")
            # O vencedor pega a carta do perdedor.
            mao_jogador.append(mao_computador.pop(0))
            # A carta usada pelo vencedor vai para o final do seu baralho.
            mao_jogador.append(mao_jogador.pop(0))
            jogador_da_vez = "jogador"
        elif valor_computador > valor_jogador:
            print("\nO computador venceu a rodada!")
            mao_computador.append(mao_jogador.pop(0))
            mao_computador.append(mao_computador.pop(0))
            jogador_da_vez = "computador"
        else:
            print("\nEmpate! As cartas foram para o fundo do baralho de cada um.")
            # Em caso de empate, cada um mantém sua carta, movendo-a para o final.
            mao_jogador.append(mao_jogador.pop(0))
            mao_computador.append(mao_computador.pop(0))

        rodada += 1
        input("\nPressione Enter para continuar...")

    # Lógica de fim de jogo.
    limpar_tela()
    if not mao_jogador:
        print("⭐⭐⭐ FIM DE JOGO! ⭐⭐⭐")
        print("Você perdeu, ficou sem cartas. Mais sorte na próxima vez!")
    else:
        print("⭐⭐⭐ FIM DE JOGO! ⭐⭐⭐")
        print("Parabéns, você venceu! O computador não tem mais cartas.")

# Ponto de entrada do script: executa a função 'jogar' quando o arquivo é rodado.
if __name__ == "__main__":
    jogar()
