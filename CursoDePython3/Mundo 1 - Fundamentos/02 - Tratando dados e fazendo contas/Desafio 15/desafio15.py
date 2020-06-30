#Desafio 15
#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por km rodado.

dias_alugados = int(input('Quantos dias alugados? '))
km_rodados = float(input('Quantos km rodados? '))
custo_total = (dias_alugados * 60) + (km_rodados * 0.15)
print('O total a pagar é de R${:.2f}'.format(custo_total))