# Operadores in e not inSenha incorreta
# Strings sao iteraveis
# 0 1 2 3 4 5
# O t a v i oSenha incorreta
# 6-5-4-3-2-1

nome = 'Otávio'
print(nome[2])
print(nome[-6])

print('vio' in nome)
print('zero' in nome)
print(10* '-')
print('vio' not in nome)
print('zero' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} esta em {nome}')
else:
    print(f'{encontrar} não esta em {nome}')

print(encontrar in nome)