import random

def jogar():
    print('adivinhe')
    print('******************')

    numero_secreto=random.randrange(1,101)
    total_tentativas=3
    pontos=1000

    nivel = int(input('Defina o nível: '))

    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas=5

    for rodada in range(1,total_tentativas+1):
        print('Tentativa {} de {}'.format(rodada, total_tentativas));
        chute = input('Digite o seu número entre 1 e 100: ')

        print('Voce digitou', chute)

        if(int(chute) < 1 or int(chute) > 100):
            print('Deve ser um número entre 1 e 100')
            continue

        acertou = numero_secreto == int(chute)
        maior = int(chute) > numero_secreto
        menor = int(chute) < numero_secreto

        if(acertou):
            print('Certo e fez {} pontos!'.format(pontos))
            break
        elif(maior):
            print('Chute acima')
            pontos_perdidos = abs(numero_secreto - int(chute))
            pontos = pontos - pontos_perdidos
        else:
            print('Chute abaixo')
            pontos_perdidos = abs(numero_secreto - int(chute))
            pontos = pontos - pontos_perdidos


if(__name__=='__main__'):
    jogar()