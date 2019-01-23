entr = int(raw_input())

soma = 0
sapo = 0
coelho = 0
rato = 0
pc = 0
pr = 0
ps = 0

while entr > 0:
    
    a,b = map(str,raw_input().split())
    
    a = int(a)
    
    soma = a + soma
    
    if b == 'C' :
        coelho += a
    
    elif b == 'S' :
        sapo += a
    
    elif b == 'R' :
        rato += a
        
    entr -= 1

pc = coelho * 100.0 / soma 
ps = sapo * 100.0 / soma 
pr = rato * 100.0 / soma 

print'Total: %i cobaias' % soma
print'Total de coelhos: %i'% coelho
print'Total de ratos: %i'% rato
print'Total de sapos: %i' % sapo
print'Percentual de coelhos: %.2f %%' % pc
print'Percentual de ratos: %.2f %%' % pr
print'Percentual de sapos: %.2f %%' % ps
