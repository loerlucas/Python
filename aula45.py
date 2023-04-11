'''
Iterável -> um elemento que pode te entregar uma coisa por vez. str, range, etc (__iter__)...
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o proximo valor
iter -> me entregue seu iterador (o ponteiro ** de onde começa o objeto)
'''

#texto = iter('Luiz')
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())

# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))


# for letra in texto
texto = 'Luiz' # iterável
# iterator = iter(texto) # Iterator

# while True:
#     try:
#         letra = next(iterator)
#         print(letra)
#     except StopIteration:
#         break

for letra in texto:
    print(letra)