
idade = input('Digite sua idade: ')

numerais = [
    '0', 
    '1', 
    '2', 
    '3', 
    '4', 
    '5', 
    '6', 
    '7', 
    '8', 
    '9'
]

for letra in idade:
    if letra in numerais:
        print('Digitou um número')
    else:
        print('Digitou um caracter não numérico')

# idade = int(idade)
