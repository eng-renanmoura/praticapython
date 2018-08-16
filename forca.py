import random

def jogar():
    imprime_msg_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0
    tentativas = 6

    while(not enforcou and not acertou):
        print('jogando...')

        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            print('Voce ainda tem {} tentativas'.format(tentativas - erros))

        enforcou = erros == tentativas
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print('Voce ganhou')
    else:
        print('Voce perdeu')

def imprime_msg_abertura():
    print('forca')
    print('******************')

def carrega_palavra_secreta():
    arquivo = open('palavras.txt', 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta

def inicializa_letras(palavra):
    return ['_' for letra in palavra]

def pede_chute():
    chute = input('Qual a letra? ')
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra):
    index = 0
    for letra in palavra:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1


if(__name__=='__main__'):
    jogar()