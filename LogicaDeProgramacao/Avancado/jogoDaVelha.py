#Crie um programa que permita a dois jogadores jogar uma partida de Jogo da Velha no terminal.

tabuleiro = [['-','-','-'],
             ['-','-','-'],
             ['-','-','-']]

jogador1= "X"
jogador2 = "0"

def mostrarTabuleiro():
    print("----------------------JOGO DA VELHA----------------------")
    for i in range(0,3):
        print(tabuleiro[i][0],"|", tabuleiro[i][1],"|",tabuleiro[i][2],"|")

def ganhar(jogador):
    for sublista in tabuleiro:
        if(all(k== sublista[0] and k !='-' for k in sublista)):
            print(f"Parabens {jogador} ganhou")
            return True
    
    for coluna in range(3):
        if(tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] !="-"):
            print(f"Parabens {jogador} ganhou")
            return True
    
    if (tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] !="-"):
        print(f"Parabens {jogador} ganhou")
        return True
    if (tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] !="-"):
        print(f"Parabens {jogador} ganhou")
        return True

for i in range(9):  
    
    if(i % 2 == 0):
        jogadorAtual = jogador1
        print("Vez do jogador 1 (X)")
    else:
        jogadorAtual = jogador2
        print("Vez do jogador 2 (0)")
    mostrarTabuleiro()
    
    jogadaValida = False 
    while not jogadaValida:
        jogadalinha = int(input("Digite o numero da sua jogada: (Exemplo, digite 1 para a primeira linha)"))
        jogadaposicao = int(input("Digite o numero da sua jogada: (Exemplo, digite 1 para a primeira posição)"))
        
        if (tabuleiro[jogadalinha][jogadaposicao] == '-'):
            tabuleiro[jogadalinha][jogadaposicao] = jogadorAtual
            jogadaValida = True
        else:
            print("Faça uma jogada valida")
        
    if ganhar(jogadorAtual):
        break

mostrarTabuleiro()
        
        
            

