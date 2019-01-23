x = 0
j = 1
for i in range (1,12):
  for i in range (1,4):
    if x == 0 or x == 1 or x == 2 or j == 1 or j == 2 or j ==3 or j == 4 or j == 5:
      print "I=%d J=%d" %(x, j)
    else:
      print "I=%.1f J=%.1f" %(x, j)
    j+=1
  x+= 0.2
  j=x+1
  if x > 1.8:
    break
  

print "I=%d J=%d" %(2, 3)
print "I=%d J=%d" %(2, 4)
print "I=%d J=%d" %(2, 5)
