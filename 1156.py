soma = 0
j=1
for i in range(1,40):
  i+=2 
  soma += i/j 
  j = j+j
print "%.2f" %(soma)
