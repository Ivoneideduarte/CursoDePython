#Desafio 07
#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.

aluno = input('Informe o nome do aluno: ')
nota1 = float(input('Nota 01: '))
nota2 = float(input('Nota 02: '))
nota3 = float(input('Nota 03: '))
nota4 = float(input('Nota 04: '))
#Ordem de precedência
media = (nota1 + nota2 + nota3 + nota4) / 4

print('Calculando nota, aguarde...')
print('{}, sua média é {}'.format(aluno, media))



