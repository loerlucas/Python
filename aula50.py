'''
Cuidados com dados mutaveis
= - copiado o valor (imutaveis)
= - apona para o mesmo valor na memoria (mutavel)
'''

nome = 'Luiz'
noutra_variavel = nome
nome = 'Joao'
print(nome)
print(noutra_variavel)

lista_a  = ['Luiz', 'Maria']
lista_b = lista_a # copia de ponteiro
lista_c = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_b)
print(lista_c)


'''
Exercício
exiba os indices da lista
'''
lista = ['Maria','Helena','Luiz']
lista.append('Joao')
indice = range(len(lista))
for ind in indice:
    print(ind, lista[ind], type[lista[ind]])



