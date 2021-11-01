limite, num_linhas = map(int,input().split())
pares = [0]*(limite + 1)
 
for i in range(num_linhas):
  cidade_a, cidade_b = map(int,input().split())
  pares[cidade_a] = 1
  pares[cidade_b] = 1
 
for i in range(1, limite + 1):
  if pares[i] == 0:
    aux = i
    break
        
print(limite - 1)
for i in range(1, limite + 1):
  if i != aux:
    print(i, aux)