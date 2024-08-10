#Crie um programa que conte quantas letras "a" existem em uma string fornecida pelo usuário.

palavra = input("Digite sua palavra: ")

letrasA = 0
for i in palavra:
    if (i=='a'):
        letrasA += 1

print(letrasA)