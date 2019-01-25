x = int(raw_input())
y = int (raw_input())
while y <= x:
  y = int (raw_input())

soma = 0
cont = 0
for i in range(x,1000):
  soma +=i
  cont += 1
  if soma > y:
    break
print "%d" %(cont)

