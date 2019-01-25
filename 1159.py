for i in range(10000):
  x= int(raw_input())
  if x == 0:
    break
  else:
    soma = 0
    for j in range(x, x + 10):
      if j%2 == 0:
       
        soma += j

    print "%d" %(soma)
