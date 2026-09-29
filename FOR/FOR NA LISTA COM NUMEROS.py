numeros = [1, 2, 3, 4, 5, 6, 7]
for n in numeros:
    if n %2 == 0:
        print("Abaixo é Par: \n", n)
    elif n in numeros:
        if n %2 != 0:
            print("Abaixo é Ímpar: \n", n)