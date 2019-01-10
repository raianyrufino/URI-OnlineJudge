dias = int(raw_input())

ano = 0
mes = 0

if dias >=30 and dias <365:
  mes = dias/30
  dias = abs(mes*30 - dias)
elif dias>=365:
  ano = dias/365
  dias = dias -ano *365
  mes = dias/30
  dias = dias - mes *30
  
print("%d ano(s)" %(ano))
print("%d mes(es)" %(mes))
print("%d dia(s)" %(dias))
