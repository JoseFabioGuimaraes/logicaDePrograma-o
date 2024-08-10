#Crie um programa que verifique se uma palavra fornecida pelo usuário é um palíndromo (lê-se da mesma forma de trás para frente).

palavra = input("Digite a palavra para verificar se é um Palíndromo: ").lower() #deixo em lower para evitar diferença na compração
palavra = palavra.replace(" ","") #removo os espaços, caso haja;

palavra_invertida = palavra[::-1]

if(palavra == palavra_invertida):
    print("A palavra é um Palíndromo")
else:
    print("Não é um Palíndromo")