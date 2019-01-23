x = int(raw_input())
y = int(raw_input())

somatoria =0
if x > y:
  for i in range (y, x+1):
    if i%13 != 0:
      somatoria += i

elif x < y:
  for i in range (x, y+1):
    if i%13 != 0:
      somatoria += i
print "%d" %(somatoria)
