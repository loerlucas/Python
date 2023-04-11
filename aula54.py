'''
Faça  uma lista de compras com listas
O usuario deve ter a possibilidade de inserir, apagar e listar
valores da sua lista.
Não permita que o programa quebre com erros de indcies inexistentes na lista.
'''

# def listagem(lista):
#     for indice, nome in enumerate(lista):
#         print(f'{indice} - {nome}')

# lista_compras = []

# while True:
#     entrada = input('[i]nserir [a]pagar [l]istar, [s]air: ')
#     if entrada.lower() == 's':
#         print('Obrigado, Volte Sempre')
#         break

#     if entrada.lower() == 'i':
#         nome = input('Igrediente a ser inserido: ')
#         lista_compras.append(nome)
#         listagem(lista_compras)
#         continue

#     if entrada.lower() == 'a':
#         indice = input('Indice a ser deletado: ')
#         if int(indice) > len(lista_compras)-1:
#             print('Entre com um indice válido')
#             continue        
#         del lista_compras[int(indice)]
#         listagem(lista_compras)
#         continue

#     if entrada.lower() == 'l':
#         listagem(lista_compras)
#         continue
   
                            
"""
Solução
"""    
import os
lista = []
while True:
    print("Selecione uma opção: ")
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao =='i':
        os.system('clear')
        valor = input('Valor: ')
        lista.append(valor)
        
    elif opcao == 'a':
        indice_srt = input('Escolha o indice para apagar: ')
        try:
            indice = int(indice_srt)
            del lista[indice]
        except ValueError:
            print('Nao foi possivel converter para int!')
        except IndexError:
            print('Nao existe este indice')
        
    elif opcao =='l':
        os.system('clear')

        if len(lista) == 0:
            print('Nada para listar')
        
        for i, valor in enumerate(lista):
            print (i, valor);
        
    else:
        print('Por Favor, escolha i, a ou l')