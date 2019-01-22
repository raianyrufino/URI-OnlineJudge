cont = 0
soma=0
for i in range(6):
  i = float(raw_input())
  if i > 0:
    cont += 1
    soma += i
    
print "%d valores positivos" %(cont)
print "%.1f" %(soma/cont)
