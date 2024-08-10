#Escreva um programa que receba cinco números inteiros e calcule a soma deles.

soma = 0

for i in range (5):
    valor = int(input(f"Digite o valor {i+1}:"))
    soma += valor

print (soma)