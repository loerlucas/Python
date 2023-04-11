# def montaResultado(palavra_secreta, letra) -> str:
#     saida = ''
#     for letra_interna in palavra_secreta:
#         if letra_interna == letra:
#             saida += letra
#         else:
#             saida += '*'
#     return saida

# def montaResultadoVazio(palavra_Secreta)-> str:
#     saida = ''
#     for letra in palavra_Secreta:
#         saida += '*'
#     return saida


# # '''
# # Faça um jogo para o susário adivinhar qual a palavra secreta.
# # - Voce vai propor um apalavra secreta qualquer e vai dar a 
# # possibilidade para  usuario digitar apenas uma letra.
# # - Quando o usuário digitar ma letra, você vai conferir se 
# # a letra digitada esta na palavra secreta.
# #     - Se a letra digitada estiver na palavra secreta; exiba a letra;
# #     - Se a letra na estiver na palavra secreta; exiba *.
# # Faça uma contagem de tentativas do seu usuario;
# # '''
# palavra_secreta = 'perfume'
# contador = 0
# letra_palpite = ''
# while True:
#     saida = ''
#     letra_palpite= input(f'entre com apenas uma Letra ({contador}x): ')
#     if len(letra_palpite) > 1:
#         print('Entre com apenas uma letra')
#         continue
#     contador += 1
#     if letra_palpite in palavra_secreta:
#         print(montaResultado(palavra_secreta, letra_palpite))
#     else:
#         print(montaResultadoVazio(palavra_secreta))
'''
Solução
'''
import os

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativa = 0
while True:
    letra_digitada =input('Digite uma Letra: ')
    numero_tentativa += 1

    if len(letra_digitada) > 1:
        print('Digite Apenas uma Letra')
        continue
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
           palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print('Palavra Formada:', palavra_formada)

    if palavra_formada ==  palavra_secreta:
        os.system('clear')
        print('VOCÊ GANHOU!! PARABENS')
        print('A palavra era: ', palavra_secreta)
        print(f'Tenativas: {numero_tentativa}')
        letras_acertadas = ''
        numero_tentativa = 0

        




