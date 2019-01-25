n = int(raw_input())
y = 0 
x = 1
fib = 0
print (y),
print (x),

if n > 0 and n < 46:
  for i in range(n-2):
    fib = y+x 
    print "%d" %(fib),
    y = x 
    x = fib
