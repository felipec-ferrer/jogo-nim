import main.py


def partida() -> Nome:
    print("O JOGO DO NIM")

    opcao_jogo = input("Insira o modo de jogo que você deseja fazer: \n[1] - Partida rápida Jogador 1 x Jogador 2\n[2] -Campeonato Joga")
    n = int(input('Insira a váriavel n: '))
    m = int(input('Insira a váriavel m: '))

    if opcao_jogo == 2:
        campeonato('j', m ,n)
    elif opcao_jogo == 4:
        campeonato('c', m,n )

    if opcao_jogo == 1:
        while n > 0
        
        
