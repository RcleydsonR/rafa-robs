def maior_rec(lista, tam):
    if (tam == 1):
        return lista[0]
    else:
        elem = maior_rec(lista, tam-1)
        if(lista[tam-1] > elem):
            return lista[tam-1]
        else:
            return elem

lista = [1,5,4,3,2]
print('O maior elemento entre:', lista)
print('Eh:', maior_rec(lista, len(lista)))
