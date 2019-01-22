x = int(raw_input())
y = int(raw_input())


if (y > x):
  soma = 0
  for i in range(x+1, y):
    if i % 2 == 1:
      soma += i
  print"%d" %(soma)
else:
  soma = 0
  for i in range(y+1, x):
    if i % 2 == 1:
      soma += i
  print"%d" %(soma)
  
