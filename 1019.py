valor = int(raw_input()) 

hora = valor/3600
resto = valor % 3600

minuto = resto / 60
restomin = resto % 60



print("%d:%d:%d" %(hora, minuto, restomin))


