n = int(raw_input())

fatorial =1 
if n > 0 and n < 13:
  for i in range (1, n+1):
    fatorial = i * fatorial
print "%d" %(fatorial)
