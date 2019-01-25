n = int(raw_input())
vetor = []
a = 0

for i in range(1000):
  print "N[%d] = %d" %(i,a)
  a += 1 
  if a == n:
    a = 0
  
