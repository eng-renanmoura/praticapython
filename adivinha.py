print('adivinhe')
print('******************')

numero_secreto=42

chute = input('Digite o seu numero: ')

print('Voce digitou', chute)

acertou = numero_secreto == int(chute)
maior = int(chute) > numero_secreto
menor = int(chute) < numero_secreto

if(acertou):
    print('Certo')
elif(maior):
    print('Chute acima')
else:
    print('Chute abaixo')
