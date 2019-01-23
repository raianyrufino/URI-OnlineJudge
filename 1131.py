inter = 0 
gremio = 0 
empates = 0 

for i in range(10000):
  x, y = map(int,raw_input().split())
  if x > y:
    inter += 1 
  if y > x:
    gremio += 1 
  if y == x:
    empates += 1
  print "Novo grenal (1-sim 2-nao)"
  valor = int(raw_input())
  if valor == 2:
    break
  elif valor == 1:
    continue
  else:
    while valor > 2 or valor <= 0:
           print "Novo grenal (1-sim 2-nao)"
           valor = int(raw_input())
  
print "%d grenais" %(inter+gremio+empates)
print "Inter:%d" %(inter)
print "Gremio:%d" %(gremio)
print "Empates:%d" %(empates)

if inter > gremio:
  print "Inter venceu mais"
elif inter < gremio:
  print "Gremio venceu mais"
