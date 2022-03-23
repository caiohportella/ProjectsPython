n = int(input("Digite o valor inteiro para n: "))
p = n

if n == 0:
    print("1")
elif n == 1:
    print("1")
else:
    while n != 1:
        p = p * (n - 1)
        n = n - 1
        if n == 1:
            print(p)
