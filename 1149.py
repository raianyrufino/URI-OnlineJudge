valores = raw_input().split()
a = int(valores[0])
i = 1

soma = 0

if int(valores[1]) == 0:
  while i < len(valores):
    if int(valores[i]) > 0:
      n = int(valores[i])
      break
    i+=1
    

for i in range(n):
  soma += (a+i)
print "%d" %(soma)
