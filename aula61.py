'''
CPF: 76.824.890-70
Colete a soma dos 9 primeiros digitos do CPF
multiplicando cada um dos valores por uma contagem regresiva comecando de 10
Ex:   746.824.890-70 (746824890)
10   9   8   7   6   5   4   3   2
7    4   6   8   2   4   8   9   0
70   36  48  56  12  20  32  27  0

soma o resultado: 70 + 36 + 48 + 56 + 12 + 20 + 32 + 27 + 0 = 301

multiplica por 10: 301 * 10 = 3010
Obtenha o resto da divisao da conta por 11
3010 % 11 = 7 
se o resultado for maior q 9: result = 0
senao

'''
import re
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



cpf_original = input('Entre com o cpf: ')
cpf_limpo = re.sub(r'[^0-9]',
                   '',
                   cpf_original)[:9]
primeiro_digito = primeiro_digito(cpf_limpo)
segundo_digito = segundo_digito(cpf_limpo, primeiro_digito)

cpf_gerado = f'{cpf_limpo[:3]}.{cpf_limpo[3:6]}.{cpf_limpo[6:9]}-{primeiro_digito}{segundo_digito}'
if(cpf_gerado == cpf_original):
    print(cpf_original, 'CPF Valido', sep=' -> ')
else:
    print(cpf_original, 'CPF Invalido', sep=' -> ')