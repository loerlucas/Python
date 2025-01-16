'''
Listas em Python
Tipo list - Mutavel
Suporta vários valores de qualquer tipo
Conhecimentos reutilizaveis - índices e fatiamento
Metodos Úteis:
    append, insert, pop, del, clear, extend, +
Create Read, Update, Delete
Criar  Ler, alterar, apagar = lista[i] (CRUD)
'''
#        0   1   2   3   4   5 
lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])

lista.append(50)
lista.pop()
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop()
lista.pop(3)
print(lista, 'Ultimo Valor: ', ultimo_valor)


"""
for in com listas    
"""

lista = ['Maria','Helena', 'Luiz']

for nome in lista:
    print(nome, type(nome))