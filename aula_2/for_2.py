
lista = [
    47,
    80,
    50,
    69,
    41,
    50,
    5,
    14,
    14,
    88,
]

soma = 0
contador = 0

for numero in lista:
    if numero % 2 == 1:
        soma = soma + numero
    contador = contador + 1
media = soma / contador

for numero in lista:
    if numero > media:
        print(numero)
        