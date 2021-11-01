from collections import deque
 
def busca(numero_n, numero_m):
  dicionario = dict()
  dicionario[numero_n] = [2 * numero_n, numero_n - 1]
 
  distancias = dict()
  distancias[numero_n] = 0
  distancias[2 * numero_n] = 1
  distancias[numero_n - 1] = 1
 
  fila = deque()
  fila += dicionario[numero_n]
 
  while True:
    elemento = fila.popleft()
    if elemento == numero_m:
      return distancias[elemento]
    elif elemento > numero_m:
      dicionario[elemento] = [elemento - 1]
    elif elemento < numero_m / 10:
      dicionario[elemento] = [elemento * 2]
    else:
      dicionario[elemento] = [2 * elemento, elemento - 1]
    for v in dicionario[elemento]:
      if distancias.get(v) is None:
        distancias[v] = distancias[elemento] + 1
    fila += dicionario[elemento]
 
numero_n, numero_m = map(int, input().split())
 
soma = 0
if numero_n >= numero_m:
  print(busca(numero_n, numero_m))
else:
  aux = numero_m
  while True:
    numero_m = aux
    aux = (aux + 1) // 2
    soma += busca(aux, numero_m)
    if aux / 2 < numero_n:
      soma += busca(numero_n, aux)
      break
  print(soma)