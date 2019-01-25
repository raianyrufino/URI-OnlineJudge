n = int(raw_input())
vetor = []
pos = 0 

vetor = map(int,raw_input().split())

for i in range(len(vetor)):
  if i == 0:
    menor = vetor[i]
    pos = i
  else:
     if vetor[i] < menor:
       menor=vetor[i]
       pos=i
    

print "Menor valor:", menor
print "Posicao: %i" %(pos)
