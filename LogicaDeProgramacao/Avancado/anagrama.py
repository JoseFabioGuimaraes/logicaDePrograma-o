#Crie um programa que determine se duas palavras fornecidas pelo usuário são anagramas (possuem as mesmas letras, mas em ordem diferente).
#LEMBRETE: NÃO ESTOU USANDO A ESTRUTURA SORTED, POR MOTIVOS DE NÃO QUERO

primeiraPalavra = input("Digite a primeira palavra: ").lower()
segundaPalavra = input("Digite a segunda palavra: ").lower()

if(len(primeiraPalavra) != len(segundaPalavra)):
    print("Não é um anagrama")

contagem = {}
contagem2= {}
for i in primeiraPalavra:
    if(i in contagem):
        contagem[i] += 1 
    else:
        contagem[i] = 1

for i in segundaPalavra:
    if(i in contagem2):
        contagem2[i] += 1 
    else:
        contagem2[i] = 1

if contagem == contagem2:
    print("As palavras são anagramas")
else:
    print("Não é um anagrama")


