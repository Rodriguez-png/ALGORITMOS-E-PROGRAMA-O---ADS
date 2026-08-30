graus = int (input("digite a temperatura atual: ")) # chama a entrada pedindo a temperatura


if graus < 7: #se for verdadeira essa condição dos graus serem menores que 7, printará congelando.
    print('Congelando') 
elif 7 <= graus <= 10: #se a condição de cima foir falsa, cairá nesta ou nas outras abaixo, dependendo de quantos graus forem digitados pelo usuario.
    print('Frio')
elif 11 <= graus <= 19:
    print('Agasalhe-se pela manhã, clima ameno durante o dia')
elif 20 <= graus <= 26:   
    print('Otimo')
else:
    print('Muito quente') # se todas condições acima forem falsas, cairá neste else para avisar ao usuario: Muito quente.

