a, b, c = map(int,raw_input().split())

crescente = [a, b, c]
normal = [a, b, c]
crescente.sort()
for numero in crescente:
  print "%d" % (numero)

print 
for numero in normal:
  print "%d" % (numero)
