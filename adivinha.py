print('adivinhe')
print('******************')

numero_secreto=42

chute = input('Digite o seu numero: ')

print('Voce digitou', chute)

if(numero_secreto == int(chute)):
    print('Certo')
else:
    print('Errado')