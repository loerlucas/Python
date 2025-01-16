import random
import sys

def primeiro_digito(cpf) -> int:
    lista_cpf = list(cpf)
    indice_inverso = 10
    soma = 0
    for i in range(len(cpf)):
        soma += int(lista_cpf[i]) * indice_inverso
        indice_inverso -= 1
    modulo_10x = (soma * 10) % 11
    return modulo_10x if modulo_10x < 10 else 0

def segundo_digito(cpf, digito_1 )-> int:
    lista_cpf = list(cpf)
    lista_cpf.append(digito_1)
    indice_inverso = 11
    soma = 0
    for i in range(len(cpf)+1):
        soma += int (lista_cpf[i]) * indice_inverso
        indice_inverso -= 1
    modulo_10x = (soma * 10) % 11
    return modulo_10x if modulo_10x < 10 else 0


for _ in range(100):
    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0,9))

    cpf_gerado = f'{nove_digitos[:3]}.{nove_digitos[3:6]}.{nove_digitos[6:9]}-{primeiro_digito(nove_digitos)}{segundo_digito(nove_digitos, primeiro_digito(nove_digitos))}'
    print(cpf_gerado)

