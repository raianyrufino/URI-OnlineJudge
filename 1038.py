cod, quant= map(int,raw_input().split())

if (cod == 1):
  total1 = 4.00*quant
  print("Total: R$ %.2f" %total1)

elif (cod == 2):
  total2 = 4.50*quant
  print("Total: R$ %.2f" %total2)
  
elif (cod == 3):
  total3 = 5.00*quant
  print("Total: R$ %.2f" %total3)
  
elif (cod == 4):
  total4 = 2.00*quant
  print("Total: R$ %.2f" %total4)
else:
  total5 = 1.50*quant
  print("Total: R$ %.2f" %total5)
  
