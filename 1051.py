valor = float(raw_input())

if valor >= 0.00 and valor <= 2000.00:
  print "Isento"
elif valor >= 2000.01 and valor <= 3000.00:
  extraum = 2000 - abs(valor) 
  taxaum = extraum * 8/100
  print "R$ %.2f" %(abs(taxaum))
elif valor > 3000 and valor <= 4500.00:
  extradois = valor - 3000 
  taxaextra = extradois * 18/100
  total = 80.00 + taxaextra
  print "R$ %.2f" %(total)
else:
  extradoiss = valor - 4500
  taxaextraa = extradoiss * 28/100
  totall = 80.00 + 270.00 + taxaextraa
  print "R$ %.2f" %(totall)
