#Desafio 08
#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

# 100m => 10.000cm => 100.000 mm
#metros = int(input('Digite um valor: '))
#metros = valor * 10
#centimetros = metros * 100
#milimetros = metros * 1000
#print('Seu valor em metros é {} m, em centimetros é {} cm e em milimetros é {} mm '.format(metros, centimetros, milimetros))

medida = float(input('Uma distância em metros: '))
km = medida / 1000
hc = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print('{}km\n {}hc\n {}dam\n {:.0f}dm\n {:.0f}cm\n {:.0f}mm'.format(km, hc, dam, dm, cm, mm))
