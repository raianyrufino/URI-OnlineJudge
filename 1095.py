x = 1
j = 60

for i in range(1000):
  j -= 5
  x += 3
  print "I=%d J=%d" %( x - 3, j + 5)
  if j == 0 - 5:
    break
