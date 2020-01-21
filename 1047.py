hi,mi,hf,mf = map(int,raw_input().split())
if hi == hf == mi == mf:
  horas, minutos = 24, 0
else:
  if mf >= mi:
    minutos = mf - mi
  else:
    minutos = 60 - abs(mf - mi)
    hf = hf - 1
  if hf >= hi:
    horas = hf - hi
  else:
    horas = 24 - abs(hf -hi)
  
print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(horas, minutos))
