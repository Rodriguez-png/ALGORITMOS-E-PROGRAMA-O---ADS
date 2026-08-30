#definicao de funcoes. O que cada uma vai fazer
def imc_formula(peso, altura):#Funcao para calcular o imc com a formula
    res = peso / (altura ** 2)
    return res

def dados_do_paciente():#Funcao para pegar os dados do paciente
    nome = input("Digite o nome do paciente: ")
    altura = float (input("Digite a sua altura:"))
    peso = float (input("Digite seu peso: "))
    return nome, altura, peso

#dps de declarar tudo e organizar cada funcao e suas definicoes, devemos chamar a func. principal
#1: pegar os dados que vamos printar na tela:
nome, altura, peso = dados_do_paciente()
#2 exibir estes dados:
print(f"\nPaciente: {nome}")
print("Altura: ", altura)
print("Peso: ", peso)

#3: calcular e exibir o IMC:
print(f"seu imc é de: {imc_formula(peso, altura):.2f}") # o .2f serve para deixar em 2 casas decimais
            #o peimeiro f serve para avisar o py que nao e uma frase comum, e que tem calculos ou variaveis dentro de chaves