import forca
import adivinha

def escolhe_jogo():
    print('escolha o jogo')
    print('******************')

    print('1 para Forca e 2 para Adivinha')

    jogo = int(input('Qual jogo?'))

    if(jogo == 1):
        print('Jogando forca')
        forca.jogar()
    else:
        print('Jogando adivinha')
        adivinha.jogar()

if(__name__=='__main__'):
    escolhe_jogo()