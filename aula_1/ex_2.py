
# Tipos primitivos

texto = 'Lucas Ricciardi de Salles'
inteiro = 27
decimais = 1.80
booleano = True # False

# Ex 2
# Solicitar ao usuário as informações:
# - nome
# - idade
# - email
# e armazenar os valores em variáveis
# (ESCOLHAM BEM OS NOMES)

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
email = input('Digite seu email: ')

# print(nome)
# print(idade)
# print(email)

if int(idade) > 18:
    print('Olá')
else:
    print('Bloqueado')
