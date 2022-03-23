def isNum(valor):
    try:
        if int(valor) or float(valor):
            return True
    except ValueError:
        print('Tente novamente com um número.')
        return False


def crescente():
    while True:
        n1 = input("Digite o primeiro número: ")
        n2 = input("Digite o segundo número: ")
        n3 = input("Digite o terceiro número: ")
        if isNum(n1) and isNum(n2) and isNum(n3):
            if n1 != n2 or n2 != n3 or n3 != n1:
                if n1 >= n2 >= n3:
                    C = n1
                    B = n2
                    A = n3

                elif n1 >= n3 >= n2:
                    C = n1
                    B = n3
                    A = n2

                elif n2 >= n1 >= n3:
                    C = n2
                    B = n1
                    A = n3

                elif n2 >= n3 >= n1:
                    C = n2
                    B = n3
                    A = n1

                elif n3 >= n1 >= n2:
                    C = n3
                    B = n1
                    A = n2

                else:
                    C = n3
                    B = n2
                    A = n1

                return print("A ordem crescente dos números é:", "A =", A, "B =", B, "C =", C)

            else:

                return print("Não há ordem crescente pois, A = B = C")
        continue

crescente()