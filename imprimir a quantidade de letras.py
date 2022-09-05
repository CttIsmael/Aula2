#Escrever uma palavra e imprimir a quantidade de letras.

def palavra(c):
    return len(c)

def main():
    c = str(input())
    print(f'{palavra(c)}')

if __name__ == "__main__":
    main()
