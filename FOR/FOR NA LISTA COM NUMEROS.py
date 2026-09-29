numeros = [1, 2, 3, 4, 5, 6]
for n in numeros:
    if n %2 == 0:
        print("Abaixo é par: \n", n)
    elif n in numeros:
        if n %2 != 0:
            print("Abaixo é impar: \n", n)