x = 1
j = 8
for i in range (1,10):
  for i in range (5,8):
    print "I=%d J=%d" %(x, j-1)
    j-=1
  x+=2
  j=8
  if x == 11:
    break
