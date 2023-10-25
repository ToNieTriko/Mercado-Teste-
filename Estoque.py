def _print_ ():
    for i in range(len(Produto)):
        print(f"\n Numero do produto({Produto[i]}): {i} ")
    return "\n"
    
def _PrintAll_ ():
    for i in range(len(Produto)):
        print (f"\n Produto: {Produto[i]} \n Valor: {Valor[i]}" )
    
def MudarValor ():
    ProdutoNum = int(input(f"{_print_()} \n Entre com o número do produto: "))
    Valor[ProdutoNum] = int(input("Entre com o novo valor: "))
    


Produto = []
Valor = []
Num = int(input("Entre com o numero de produtos: "))
for i in range(Num):
    Produto.append(input("Entre com o nome do produto: "))
    Valor.append(int(input("Entre com o valor do produto: ")))

Confirmacao = 2 
while Confirmacao !=0: 
    
    Confirmacao = int(input("digite (0) caso esteja tudo certo, ou digite (1) caso queira fazer uma modificação: "))

    if Confirmacao == 1: 
        MudarValor()
    else: 
        _PrintAll_()