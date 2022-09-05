#Calcular um valor inteiro e converter o total de segundos em formato de horas, minutos e segundos.

def converte(seg):
    hora = seg // 3600
    minutos = (seg % 3600) // 60
    segundos = (seg % 3600) % 60

    return f'{hora}:{minutos}:{segundos}'

def main():
    seg = int(input())
    total = converte(seg)
    print(total)

if __name__ == "__main__":
    main()
