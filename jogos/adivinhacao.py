import random

print('********************************')
print("Bem vindo ao jogo de Adivinhação")
print('********************************')

numero_secreto = random.randrange(1, 101) # 0.0 - 1.0
total_de_tentativas = 3
pontos = 1000

print('Qual o nível de dificuldade: ')
print('[1] - Facil [2] - Medio [3] - Dificil')

nivel = int(input('Defina o nível: '))

if nivel == 1:
    total_de_tentativas = 20
elif nivel == 2:
    total_de_tentativas = 10
else:
    total_de_tentativas = 5
    

for rodadas in range(1,total_de_tentativas+1):
    try:
        print(f'Tentativa {rodadas} de {total_de_tentativas}:{numero_secreto}')
        chute = int(input('Digite um número entre 1 e 100: '))
        print(f'Você digitou {chute}')

        acertou = chute == numero_secreto
        maior = chute > numero_secreto

        if not 0 < chute < 101:
            print('Voce deve digitar um numero entre 1 a 100!')
            continue

        if acertou:
            print(f'Você acertou e fez {int(pontos)} pontos!')
            break
        else:
            if maior:
                print('Você errou! O seu chute foi maior que o numero secreto.')
            else:
                print('Você errou! O seu chute foi menor que o numero secreto.')
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos
    except:
        print('Dados de entrada errado. Entre com um numero válido')
        
print(f'Fim do Jogo\n O numero era {numero_secreto}')
