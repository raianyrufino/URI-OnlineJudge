x = int(raw_input())

if (x > 2) and (x < 1000):
  for i in range(1,11):
    multi = i * x
    print "%d x %d = %d" %(i, x, multi)
