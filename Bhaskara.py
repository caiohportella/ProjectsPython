import math

def delta(a, b, c):
    return b ** 2 - 4 * a * c

def main():
    a = float(input("Digite um valor para a: "))
    b = float(input("Digite um valor para b: "))
    c = float(input("Digite um valor para c: "))
    imprime_raízes(a, b, c)

def imprime_raízes(a, b, c):
    delta = delta(a, b, c)
    if delta == 0:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        print("A única raiz é: ", raiz1)
    else:
        if delta < 0:
            print("Esta equação não posssui raízes reais.")
        else:
            raiz1 = (-b + math.sqrt(delta)) / (2 * a)
            raiz2 = (-b - math.sqrt(delta)) / (2 * a)
            print("A primeira raiz é: ", raiz1)
            print("A segunda raiz é: ", raiz2)
