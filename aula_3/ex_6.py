
def mapa(numero):
    if numero % 2 == 0:
        return numero * 2
    return numero * 3

def meu_mapa(lista):
    return list(map(mapa, lista))

lista_1 = [ 1, 2, 3, 4, 5 ]
print(lista_1)
lista_2 = meu_mapa(lista_1)
print(lista_2)
