maior = 0
valor = []

for i in range(100):
  valor.append(int(raw_input()))
    
for i in range(100):
  if valor[i] > maior:
    maior = valor[i]
    posicao = i
    
    
   

print "%d" %(maior)
print "%d" %(posicao+1)
