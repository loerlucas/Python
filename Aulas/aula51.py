'''
Introdução ao desempacotamento
'''
nomes = ['Maria', 'Helena', 'Luiz']
_, nome2, *_ = nomes
nome1, *_ = nomes
_, _, nome3 = nomes
print(nome1, nome2, nome3)