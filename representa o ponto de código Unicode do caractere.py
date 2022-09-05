#retorna um inteiro que representa o ponto de código Unicode do caractere quando o argumento é um objeto Unicode, ou o valor do byte quando o argumento é uma string de 8 bits.

def palavra(a):
    return ord(a)

def main():
    a = str(input())
    print(f'{palavra(a)}')

if __name__ == "__main__":
    main()
