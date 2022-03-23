def isInt(valor):
    try:
        if int(valor):
            return True
    except ValueError:
        return False


def isFloat(valor):
    try:
        if float(valor):
            return True
    except ValueError:
        return False


def pessoas(n):
    idade_50 = 0
    soma_altura = 0
    num_10_20 = 0
    peso_40 = 0
    for i in range(1, n + 1):
        idade = input(f"Digite a idade da {i}º pessoa: ")
        while isInt(idade) is False or int(idade) <= 0:
            idade = input("Tente novamente com um número inteiro de idade: ")
        altura = input(f"Digite altura da {i}º pessoa: ")
        while isFloat(altura) is False or float(altura) < 1 or float(altura) > 2.3:
            altura = input("Tente novamente com um número entre 1.0 e 2.3: ")
        peso = input(f"Digite o peso da {i}º pessoa: ")
        while isFloat(peso) is False or int(idade) <= 0:
            peso = input("Tente novamente com um número: ")
        if int(idade) >= 50:
            idade_50 += 1
        elif 10 <= int(idade) <= 20:
            soma_altura += float(altura)
            num_10_20 += 1
        elif int(peso) <= 40:
            peso_40 += 1
    return idade_50, soma_altura, num_10_20, peso_40

funcao = pessoas(5)
print("A quantidade de pessoas com idade maior de 50 é", funcao[0])
if funcao[2] == 0:
    print("Não há pessoas com idade entre 10 e 20 anos.")
else:
    print("A média das alturas das pessoas com idade entre 10 e 20 anos é de", funcao[1] / funcao[2])
print(f"A porcentagem de pessoas com peso inferior a 40 quilos é de {(funcao[3] / 5)*100}%.")