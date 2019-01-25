vetor = []


for i in range(100):
  vetor.append(input())

for i in range(100):
  if vetor[i] <= 10:
    print "A[%d] =" %(i), float(vetor[i])
