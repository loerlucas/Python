# senha_salva = '123456'
# senha_digitada = ''
# repeticoes = 0
# i = 0

# while senha_salva !=  senha_digitada:
#     senha_digitada = input(f'Sua Senha ({repeticoes}x): ')

#     repeticoes += 1

# print('Aquele laço acima pode ter repeticçoes infinitas')

novo_texto = ''
texto = 'Python'

for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto)
