#x1, x2 e x3 são as entradas binarias 
def neuronio_MP(x1, x2, x3):

    #u recebe o cálculo de MP, como todos os pesos são 1 não é necessário fazer o produto x*w    
    u = x1+x2+x3
#Verifica e gera a saída
    if u>=2:
        return 1

    return 0
    
#testando a função
teste = neuronio_MP(1, 1, 0)
print(teste)
teste = neuronio_MP(1, 1, 1)
print(teste)
teste = neuronio_MP(0, 0, 0)
print(teste)
teste = neuronio_MP(1, 0, 0)
print(teste)