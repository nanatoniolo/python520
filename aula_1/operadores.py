
# Operações entre números (int e float)

a = 2.5
b = 10

print(a + b)    # SOMA
print(a - b)    # SUBTRAÇÃO
print(a * b)    # MULTIPLICAÇÃO
print(a / b)    # DIVISÃO
print(a % b)    # MÓDULO (RESTO DA DIVISÃO)
print(a ** b)   # EXPONENCIAÇÃO

# Operações entre booleanos

x = True
y = False

print(x and y)
print(x or y)
print(not x)

# Operações entre strings

first_name = 'Lucas'
last_name = 'Ricciardi de Salles'

# Concatenação
print(first_name + ' ' + last_name)

# Interpolação
mensagem = 'Olá, {},seja bem vindo'.format(
    first_name
)
print(mensagem)

