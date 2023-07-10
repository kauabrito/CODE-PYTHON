n1 = float(input('Escreva um número em METRO que eu irei converter em CENTÍMETRO E MILÍMETRO '))
kilo = n1*0.001
hec =  n1*0.01
deca = n1*0.1
deci = n1*10
cent = n1*100
mili = n1*1000
print('{}m é {}cm ou {}mm'.format(n1, cent, mili))
print('{}km'.format(kilo))
print('{}hm'.format(hec))
print('{}dam'.format(deca))