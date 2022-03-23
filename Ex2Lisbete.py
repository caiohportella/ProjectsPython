numeroInimigo = 0
listaEntrada = []

while True:
    try:
        numero = int(input("Insira um numero(0 para sair): "))
        if(numero == 0):
            break
        listaEntrada.append(numero)
    except:
        print("Input nao consiste em um numero inteiro")
        continue

for i in range(len(listaEntrada)):
    for j in range(i + 1, len(listaEntrada)):
        if(listaEntrada[i] + listaEntrada[j]) % 11 == 0:
            numeroInimigo += 1
print("Ha um total de: "+ str(numeroInimigo) +" pares de numeros inimigos")