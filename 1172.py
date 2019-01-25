i = 0
vetor = []

for i in range(10):
  vetor.append(input())

for i in range(10):
  if vetor[i] <= 0:
    print "X[%d] =" %(i), "1"
  else:
    print "X[%d] =" %(i), vetor[i]
