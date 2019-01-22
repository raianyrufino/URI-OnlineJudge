a, b = map(int,raw_input().split())

TEMPO=24-a+b;
 
if TEMPO > 24:
  print "O JOGO DUROU %d HORA(S)" % (TEMPO-24)
elif a == b:
  print "O JOGO DUROU 24 HORA(S)"
else:
  print "O JOGO DUROU %d HORA(S)" % (TEMPO)
  
