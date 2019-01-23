n = int(raw_input())

for i in range (n):
  x, y = map(float, raw_input().split())
  if (y == 0):
    print "divisao impossivel"
  else:
    div = x/y
    print "%.1f" %(div)
