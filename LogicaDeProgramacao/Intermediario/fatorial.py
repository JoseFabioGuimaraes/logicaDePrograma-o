#Escreva um programa que calcule o fatorial de um número fornecido pelo usuário.

numero = int(input("Digite o número que deseja fatorar: "))

resultado = 1
if(numero == 0):
    print(f"Fatorial de 0 é: 1")
else:
    for i in range(1,numero+1):
       resultado *= i
    print(resultado)
