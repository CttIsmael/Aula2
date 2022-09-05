#Coletar 5 números e imprimir o maior valor, em seguida do menor valor e a média dos valores dividida por 5.

def calculo():
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    n4 = int(input())
    n5 = int(input())

    print(max(n1, n2, n3, n4, n5))
    print(min(n1, n2, n3, n4, n5))
    print((n1+n2+n3+n4+n5)/5)

def main ():
    calculo()

if __name__ == '__main__':
    main()
