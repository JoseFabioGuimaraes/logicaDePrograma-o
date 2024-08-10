voltas =  int(input("Digite quantos números deseja adicionar nessa lista: "))
i = 0
listaNumero = []
while(i<voltas):
    numero = int(input(f"Digite o {i+1}° número: "))
    listaNumero.append(numero)
    i+=1

ordenado = []
for k in range(len(listaNumero)):
    trocou = False
    for i in range(len(listaNumero)-1):
        if(listaNumero[i] > listaNumero[i+1]):
            listaNumero[i], listaNumero[i+1] = listaNumero[i+1], listaNumero[i]
            trocou = True
    if trocou == False:
        break
        
print(listaNumero)
    
        