contpar = 0
contim = 0
contpos = 0
contneg = 0
for i in range(5):
  i = int(raw_input())
  if i % 2 == 0:
    contpar += 1
  else:
    contim += 1
  if i > 0:
    contpos += 1
  elif i < 0:
    contneg += 1
  
    
print "%d valor(es) par(es)" %(contpar)
print "%d valor(es) impar(es)" %(contim)
print "%d valor(es) positivo(s)" %(contpos)
print "%d valor(es) negativo(s)" %(contneg)

