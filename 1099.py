n = int(raw_input())

soma= 0
for i in range (n):
  x, y = map(int,raw_input().split())
  if y > x:
    somax = 0
    for i in range (x+1,y):
      if i%2 ==1:
       somax += i
    print "%d" %(somax) 
    
  
  else:
    somay = 0
    for i in range (y+1,x):
      if i%2 ==1:
        somay += i
    print "%d" %(somay)
