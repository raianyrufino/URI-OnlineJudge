x = int(raw_input())

a = 1
b = 1 
c = 1
e = 1 
f = 1
for i in range(x):
  for i in range(1,2):
    print "%d %d %d" %(a, b, c)
    e = b+1
    f = c+1
    print "%d %d %d" %(a, e, f)
  a += 1
  b = a * a 
  c = a * b 
  e = b+1
  f = c+1
  if b == 126:
    break
