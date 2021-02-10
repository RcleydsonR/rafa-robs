def fatorial(qtd):
    if(qtd <= 0):
        return 1
    else:
        return qtd * fatorial(qtd-1)

num = int(input('Digite o num que deseja fatorar:'))
print(fatorial(num))
