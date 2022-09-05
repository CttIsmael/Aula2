#Imprimir valor com desconto por ser à vista e adicionais com valores de 5x e 10x.

def preco():
    preco = int(input())
    avista = preco - ((preco/100) * 9)
    cincox = preco / 5
    dezx = (preco + ((preco/100) * 17)) / 10
    print("%.2f" % avista)
    print("%.2f" % cincox)
    print("%.2f" % dezx)

def main():
    preco()

if __name__ == '__main__':
    main()
