num_intersecoes = int(input())
atalhos = list(map(int, input().split()))
 
atalhos = [(atalho - 1) for atalho in atalhos]
custos = [0] + ([-1] * (num_intersecoes - 1))
 
aux, fila = 0, [0]
while (aux < len(fila)):
    intersecao = fila[aux]
    atalho = atalhos[intersecao]
 
    if custos[atalho] == -1:
        custos[atalho] = custos[intersecao] + 1
        fila.append(atalho)
 
    if intersecao < (num_intersecoes - 1):
        if custos[intersecao + 1] == -1:
            custos[intersecao + 1] = custos[intersecao] + 1
            fila.append(intersecao + 1)  
 
    if intersecao > 0:
        if custos[intersecao - 1] == -1:
            custos[intersecao - 1] = custos[intersecao] + 1
            fila.append(intersecao - 1)
 
    aux += 1
 
print(' '.join(map(str, custos)))