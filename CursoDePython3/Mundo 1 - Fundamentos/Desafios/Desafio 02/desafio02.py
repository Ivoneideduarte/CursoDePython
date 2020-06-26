#Desafio 02
#Faça um programa que leia o dia, o mês e o ano de nascimento de uma pessoae mostre uma mensagem com a data formatada.

nome = input('Informe o seu nome: ')
print('Informe seus dados de nascimento, abaixo:')
dia = input('Dia: ')
mes = input('Mês: ')
ano = input('Ano: ')
print('Você nasceu no dia ', dia + '/' + mes + '/' + ano + '.', 'correto, ', nome + '?')