n = int(raw_input())
contin = 0
contout = 0

for i in range (n):
  x = int(raw_input())
  if (x >= 10) and (x <= 20):
    contin += 1
  else:
    contout +=1

print "%d in" %(contin)
print "%d out" %(contout)
