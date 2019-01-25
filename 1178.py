vetor = []
vetor.append(input())
n = 2.0
for i in range(100):
  vetor.append(vetor[i]/n)
  print "N[%i] = %.4f" %(i, vetor[i])
