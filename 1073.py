x = int(raw_input())


if (x > 5) and (x < 2000):
  for i in range(1,x+1):
    if i % 2 == 0:
      raiz = i*i
      print"%d^2 = %d" %(i,raiz)
