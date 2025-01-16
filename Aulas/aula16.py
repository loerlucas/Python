# if / elif      / else
# se / se nao se / se nao

entrada = input('Voce quer "entrar" ou "sair"? ')

if entrada == 'entrar':
    print('Voce entrou no sistema')
    print(12345432)
elif entrada == 'sair':
    print('Voce saiu do sistema')
else:
    print('Voce nao digito nem "entrar" nem "sair"')
print('FORA DO BLOCO')