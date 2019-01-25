soma = 0
somatoria = 0
for i in range(10000):
  idade = int(raw_input())
  if idade > 0:
    somatoria += idade
    soma += 1 
    soma = float(soma)
  if idade < 0:
    break
print "%.2f" %(somatoria/soma)
