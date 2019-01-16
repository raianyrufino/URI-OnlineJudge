valor = float(raw_input()) 

nota100 = valor/100
resto = valor % 100

nota50 = resto/50
resto50 = resto % 50

nota20 = resto50/20
resto20 = resto50 %20

nota10 = resto20/10
resto10 = resto20 % 10

nota5 = resto10/5
resto5 = resto10 % 5

nota2 = resto5/2
resto2 = resto5 % 2

moeda1 = resto2/1
restomo1 = resto2 % 1

moeda50 = restomo1/0.50
restomo50 = restomo1 % 0.50

moeda25 = restomo50 / 0.25
restomo25 = restomo50 % 0.25

moeda10 = restomo25/0.10
restomo10 = restomo25 % 0.10

moeda05 = restomo10/0.05
restomo05 = restomo10 % 0.05

moeda01 = restomo05/0.01



print "NOTAS:"
print "%d nota(s) de R$ 100.00" % (nota100)
print "%d nota(s) de R$ 50.00" % (nota50)
print "%d nota(s) de R$ 20.00" % (nota20)
print "%d nota(s) de R$ 10.00" % (nota10)
print "%d nota(s) de R$ 5.00" % (nota5)
print "%d nota(s) de R$ 2.00" % (nota2)
print "MOEDAS:"
print "%d moeda(s) de R$ 1.00" % (moeda1)
print "%d moeda(s) de R$ 0.50" % (moeda50)
print "%d moeda(s) de R$ 0.25" % (moeda25)
print "%d moeda(s) de R$ 0.10" % (moeda10)
print "%d moeda(s) de R$ 0.05" % (moeda05)
print "%.0f moeda(s) de R$ 0.01" % (moeda01)
