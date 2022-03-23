import sys

def isInt(valor):
    try:
        if int(valor):
            return False
    except ValueError:
        return True


def dados(defDados):
    if defDados:
        nome = input("Digite o seu nome inteiro: \n").capitalize().split()
        ra = input(f"{nome[0]}, digite o número de sua matricula (RA): \n")
        while isInt(ra):
            ra = input(f"{nome[0]} digite uma sequência de números válidos: \n")
        senha = input(f"{nome[0]} digite a sua senha: ")
        tentativas = 3
        while senha != "python" and tentativas != 1:
            tentativas -= 1
            senha = input(f"Senha inválida. Você possui agora apenas {tentativas} tentativas.\nDigite novamente: \n")
        if tentativas > 1:
            return
        else:
            print("Número de tentativas excedido. Conta bloqueada.")
            sys.exit()
    else:
        return


def op(saldo = 0):
    opcoes = input("Escolha o que deseja fazer:\n"
                    "1. Depósito;\n"
                    "2. Retirada; \n"
                    "3. Saldo;\n"
                    "4. Saída.\n")
    while opcoes not in ["1", "2", "3", "4"] or (opcoes == "2" and saldo == 0):
        if opcoes == "2":
            opcoes = input("Impossível a retirada de dinheiro da conta com o saldo igual a zero."
                            "\nTente novamente outra opção ou saia do programa: ")
        else:
            opcoes = input("Digite um opção válida: ")
    if opcoes == "1": 
        return 1
    elif opcoes == "2":  
        return 2
    elif opcoes == "3":  
        return 3
    else:
        print("Fim da operação.")
        sys.exit()


def dep():
    deposito = input("Digite o valor que deseja ser depositado: \n")
    while True:
        if isInt(deposito):
            deposito = input("Digite apenas números inteiros maiores que zero: \n")
        elif int(deposito) == 0:
            deposito = input("Valor igual a zero bloqueado. \nTente novamente: \n")
        elif int(deposito) < 0:
            deposito = input("Valor negativo bloqueado. \nTente novamente: \n")
        else:
            return int(deposito)


def ret():
    retirada = input("Digite o valor que deseja ser retirado: \n")
    while True:
        if isInt(retirada):
            retirada = input("Digite apenas números inteiros maiores que zero: \n")
        elif int(retirada) == 0:
            retirada = input("Valor igual a zero bloqueado. \nTente novamente: \n")
        elif int(retirada) < 0:
            retirada = input("Valor negativo bloqueado. \nTente novamente: \n")
        else:
            return int(retirada)


def chama_def(opcao, saldo):
    if opcao == 1:
        saldo += dep()
    elif opcao == 2:
        saldo -= ret()
    else:
        print("O seu saldo na conta é de:R$", saldo)
    return saldo

def faz_loop(saldo):
    loop = input("Digite 1 para sair do programa.\n"
                 "Digite 2 para continuar as operações.\n")
    while loop not in ["1", "2"]:
        loop = input("\nTente novamente com uma opção válida:\n")
    if loop == "1":
        print("\nFim da operação.")
        sys.exit()
    else:
        defDados = False
        main(saldo, defDados)

def main(saldo = 0, defDados = True):
    dados(defDados)
    opcao = op(saldo)
    saldo = chama_def(opcao, saldo)
    faz_loop(saldo)
    
main()