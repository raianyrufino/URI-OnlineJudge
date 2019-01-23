for i in range (10000):
  x, y = map(int, raw_input().split())
  if x == y:
    break
  if (x > y):
    print "Decrescente"
  if (x < y):
    print "Crescente"
