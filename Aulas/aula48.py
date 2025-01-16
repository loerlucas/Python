'''
Lista em Python
Tipo list - Mutável
Suporta vários valores de quaquer tipo
Conhecimento reutilizaveis - indices e fatiamento
Metodos uteis: 
    append - Adiciona um item ao final  
    insert - Adiciona um item no indice escolhido
    pop - Remove do final ou no índice escolhido
    del - apaga um indice
    clear - limpa a lista
    extend - estende a lista
    + - Concatena lista - polimorfismo
Create, Read, Update, Delete
Criar,  Ler,  Alterar, Apagar = lista[i] (CRUD)
'''
#.........01234
#........-54321
# # string = 'ABCDE'  # 5 caracteres len()

# # lista1 = list() # falsy
# # # print(lista1, type(lista1))

# #        0   1    2   3
# #       -4   -3  -2  -1       
# lista = [10, 20, 30, 40]
# lista.append('Luiz')
# nome = lista.pop()
# lista.append(1233)
# del lista[-1]
# # lista.clear()
# lista.insert(0,5)
# print(lista)


lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b
lista_d = lista_a.extend(lista_b)
print(lista_a)
print(lista_c)

