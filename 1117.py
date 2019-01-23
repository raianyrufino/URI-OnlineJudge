soma=0
cont = 0
for i in range (10000):
  x = float(raw_input())
  if x > 0 and x <= 10:
    soma += x
    cont +=1
    if cont == 2:
      break
  else:
    print "nota invalida"
  
print "media = %.2f" %(soma/2)
