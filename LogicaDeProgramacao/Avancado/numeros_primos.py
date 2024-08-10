#Escreva um programa que encontre todos os números primos entre 1 e 100.
listaPrimos = []
for i in range(2, 101):
    for k in range(2,int(i**0.5)+1):
        if(i%k==0):
            break
    else:
        listaPrimos.append(i)

print(listaPrimos)

