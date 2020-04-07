coluna = int(raw_input())
operacao = raw_input()   
soma = 0

for i in range(12):
    for j in range(12):
        valor = float(raw_input())
        if(j == coluna):
            soma += valor
               
if(operacao == 'S'):
     print("%.1f" %soma)
else:
     print("%.1f" %(soma/12.0))
