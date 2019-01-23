soma=0
cont = 0
for i in range (10000):
  x = float(raw_input())
  if x > 0 and x <= 10:
    soma += x
    cont +=1
    if cont == 2:
      print "media = %.2f" %(soma/2)
      print "novo calculo (1-sim 2-nao)"
      cont = 0
      soma = 0
      valor = int(raw_input())
      if valor == 2:
        break
      elif valor == 1:
        continue
      else:
        while valor > 2 or valor <= 0:
           print "novo calculo (1-sim 2-nao)"
           valor = int(raw_input())

  else:
    print "nota invalida"
