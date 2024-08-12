#Implemente o algoritmo de busca binária para encontrar um elemento em uma lista ordenada de números inteiros.

lista = [34, 7, 23, 32, 5, 62, 19, 18]

procura = int(input("Digite o valor que deseja procurar: "))

lista = sorted(lista) #[5, 7, 18, 19, 23, 32, 34, 62]


inicio = 0
fim = len(lista) - 1

while inicio <= fim:
    meio = (inicio + fim) //2

    if (lista[meio] == procura):
        print(f"O número de procura está na posição {meio+1}")
        break
    elif (lista[meio]<procura):
        inicio= meio+1
    else:
        fim = meio -1 

if(inicio>fim):
    print("Item não encontrado")

