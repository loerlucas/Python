'''
Operacao Ternaria (condicional de uma linha)
<valor> if <condicao> else <outro valor>

'''
# codicao = 10 == 10
# variavel = 'Valor' if codicao else 'Outro Valor'
# print(variavel)

digito = 10
# novo_digito = digito if digito <= 9 else 0
novo_digito = 0 if digito > 9 else digito
print(novo_digito)

print('Valor' if False else 'Outro Valor' if False else 'Fim')