#Desafio 13
#Faça um algoritmo que leia o sálario de um funcionário e mostre seu novo salário, com 15% de aumento.

funcionario = input('Nome do funcionário: ')
salario = float(input('Informe seu salário: R$ '))
desconto  = salario * 1.15
print('{} você ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f} '.format(funcionario, salario, desconto))
