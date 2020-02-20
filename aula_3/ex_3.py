
def maior_entre_dois_numeros(a, b):
    return a if a > b else b        # ternário
        
def encontrar_o_maior_numero(lista_de_numeros):
    maior_numero = lista_de_numeros[0]
    for numero in lista_de_numeros:
        maior_numero = maior_entre_dois_numeros(
            maior_numero,
            numero
        )
    return maior_numero


lista_de_notas = [ 1, 2, 3, 4, 5, 6 ]
maior_nota = encontrar_o_maior_numero(lista_de_notas)