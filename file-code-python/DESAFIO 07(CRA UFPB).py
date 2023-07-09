#calcular o meu CRA DA UNIVERDADE
print('=== CRA UFPB ===')
print('O CRA É COMPOSTO POR UMA MÉDIA DE 7 MÉDIAS DO SEMETSRE')
q1 = int(input('QUANTAS PROVAS TEM A 1° CADEIRA '))
n1 = float(input('Escreva sua primeira nota da 1°CADEIRA '))
n2 = float(input('Escreva sua segunda nota da 1°CADEIRA '))
n3 = float(input('Escreva sua terceira nota da 1°CADEIRA '))
m1 = (n1+n2+n3)/q1
q2 = int(input('QUANTAS PROVAS TEM A 2° CADEIRA '))
no1 = float(input('Escreva sua primeira nota da 2°CADEIRA '))
no2 = float(input('Escreva sua segunda nota da 2°CADEIRA '))
no3 = float(input('Escreva sua terceira nota da 2°CADEIRA '))
m2 = (no1+no2+no3)/q2
q3 = int(input('QUANTAS PROVAS TEM A 3° CADEIRA '))
not1 = float(input('Escreva sua primeira nota da 3°CADEIRA '))
not2 = float(input('Escreva sua segunda nota da 3°CADEIRA '))
not3 = float(input('Escreva sua terceira nota da 3°CADEIRA '))
m3 = (not1+not2+not3)/q3
q4 = int(input('QUANTAS PROVAS TEM A 4° CADEIRA '))
nota1 = float(input('Escreva sua primeira nota da 4°CADEIRA '))
nota2 = float(input('Escreva sua segunda nota da 4°CADEIRA '))
nota3 = float(input('Escreva sua terceira nota da 4°CADEIRA '))
m4 = (nota1+nota2+nota3)/q4
q5 = int(input('QUANTAS PROVAS TEM A 5° CADEIRA '))
test1 = float(input('Escreva sua primeira nota da 5°CADEIRA '))
test2 = float(input('Escreva sua segunda nota da 5°CADEIRA '))
test3 = float(input('Escreva sua terceira nota da 5°CADEIRA '))
m5 = (test1+test2+test3)/q5
q6 = int(input('QUANTAS PROVAS TEM A 6° CADEIRA '))
t1 = float(input('Escreva sua primeira nota da 6°CADEIRA '))
t2 = float(input('Escreva sua segunda nota da 6°CADEIRA '))
t3 = float(input('Escreva sua terceira nota da 6°CADEIRA '))
m6 = (t1+t2+t3)/q6
q7 = int(input('QUANTAS PROVAS TEM A 7° CADEIRA '))
te1 = float(input('Escreva sua primeira nota da 7°CADEIRA '))
te2 = float(input('Escreva sua segunda nota da 7°CADEIRA '))
te3 = float(input('Escreva sua terceira nota da 7°CADEIRA '))
m7 = (te1+te2+te3)/q7
cra = (m1+m2+m3+m4+m5+m6+m7)/7
print('O SEU CRA FOI {:.2f}'.format(cra))
