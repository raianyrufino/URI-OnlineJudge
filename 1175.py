vetor = []


for i in range(20):
  vetor.append(input())
  
for i in range(10):
  temp = vetor[i]
  vetor[i]= vetor[19-i]
  vetor[19-i] = temp
  
for i in range(20):
  print "N[%d] = %d" %(i, vetor[i])
