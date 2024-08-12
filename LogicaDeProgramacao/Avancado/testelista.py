lista = [[1,0,1], [1,0,0], [1,1,1]]

for sublista in lista:
    # Verifica se todos os elementos da sublista são iguais ao primeiro elemento
    if all(k == sublista[0] for k in sublista):
        print("Ganhou")
    else:
        print("Não")
