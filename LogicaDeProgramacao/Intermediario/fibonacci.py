#Escreva um programa que imprima os primeiros 20 números da sequência de Fibonacci.
a = 0
b= 1

for i in range(20):
    print(a)
    x= a
    a = b
    b = x+b
