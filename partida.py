def partida() -> None:
    print("O JOGO DO NIM")

    opcao_jogo = int(input("Insira o modo de jogo que você deseja fazer: \n[1] - Partida rápida Jogador 1 x Jogador 2\n[2] - Campeonato Joga"))
    n = int(input('Insira a quantidade total de peças no jogo: '))
    m = int(input('Insira a quantidade máxima de peças que podem ser retiradas: '))
    print("Coletou as variaveis n, m")
    
    if opcao_jogo == 2:
        campeonato('j', m ,n)
    elif opcao_jogo == 4:
        campeonato('c', m, n)
    print("Validou se é campeonato")
    
    if opcao_jogo == 1:
        j1 = input("Insira o nome do jogador 1: ")
        j2 = input("Insira o nome do jogador 2: ")
        print("")
        while n > 0:
            n = usuario_escolhe_jogada(n, m, j1)
            
            if n < 1:
                break
            
            n = usuario_escolhe_jogada(n, m, j2)

def usuario_escolhe_jogada(n: int, m: int, j: str) -> int:
    pecas_remover = int(input(f"Jogador {j}, insira a quantidade de peças que deseja remover, sendo no máximo {m}"))

    while pecas_remover > m:
        pecas_remover = int(input(f"A quantidade de peças inseridas foi maior que {m}\nInsira uma quantidade válida: "))
        
    pecas_restantes = n - pecas_remover

    if pecas_restantes < 1:
        print(f"O jogador {j} ganhou!")

    return pecas_restantes








# codigo main
partida()
print("função partida foi encerrada")
