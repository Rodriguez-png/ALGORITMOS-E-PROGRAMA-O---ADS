#VARIAVEIS
premium = 1
comum = 2
taxaPremium = 10
taxaComum = 15
valorFinalPremium = float
distanciaKm = float
valorFinalComum = float
KonstanteKM = 0.60
KonstantePeso = 1.10
FreteBasicoComum = float
gasolinaPorKm = 0.85
CustoMinimoGasolina = float

#ENTRADA DADOS
tipoDeCliente = int (input('Digite o seu nivel, para Premium pressione (1) para comum, (2): '))
# se for premium
if tipoDeCliente == premium:
    print('Cliene premium selecionado.')
    valorProduto = int(input('Informe o valor do produto: '))
    if valorProduto <= 200:
        valorFinalPremium = valorProduto + taxaPremium
        print('Valor final de: ', valorFinalPremium)
    else:
        print('Valor final de:', valorProduto)
  # se for cliente comum      
elif tipoDeCliente == comum:
    print('Cliente comum selecionado')
    valorProduto = int(input('Informe o valor do produto: '))
    pesoProduto = float(input('Informe o peso do produto: '))
    distanciaKm = float(input('Informe a distancia ate o distino: '))
    FreteBasicoComum = (taxaComum + distanciaKm * KonstanteKM + pesoProduto * KonstantePeso) #formula para saber o frete basico do cliente comum
    CustoMinimoGasolina = distanciaKm * gasolinaPorKm #Calcula o custo minimo de combustivel a partir dos quantos Km é o distino final.
    
    #ver se o frete calculado é menor que o custo de gasolina, se for menor, para a empresa nao sair perdendo, temos que igualar ao custo de gasolina anterior.
    if FreteBasicoComum < CustoMinimoGasolina:
        print('Aviso: O frete foi ajustado para cobrir os custos de combustível. ') 
    
    
    valorFinalComum = FreteBasicoComum + valorProduto
    
    print('O frete basico é de: ', FreteBasicoComum)
    print('O Valor final do produto com o frete é de: ', valorFinalComum)
    
else:
    print('faça seu cadastro!')
        
