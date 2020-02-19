
# A lista

lista = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]

soma = 0
contador = 0

for numero in lista:
    soma = soma + numero
    contador = contador + 1
    
media = soma / contador

print(media)