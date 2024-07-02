idade = int(input('coloque sua idade: '))

if idade < 0:
    print('idade invalida, coloque um número positivo')
if idade <= 12:
    print('você é uma criança')
elif idade <= 18:
    print('você é um adolescente')
else:
    print('você é um adulto')

