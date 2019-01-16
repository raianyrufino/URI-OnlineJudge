A,B,C = map(float,raw_input().split())

dec = [A, B, C]
dec.sort(reverse=True)

if (dec[0] >= dec[1] + dec[2]):
  print "NAO FORMA TRIANGULO"
elif (dec[0]*dec[0] == dec[1]*dec[1] + dec[2]*dec[2]):
  print "TRIANGULO RETANGULO"
elif (dec[0]*dec[0] > dec[1]*dec[1] + dec[2]*dec[2]):
  print "TRIANGULO OBTUSANGULO"
elif (dec[0]*dec[0] < dec[1]*dec[1] + dec[2]*dec[2]):
  print "TRIANGULO ACUTANGULO"

if (dec[0] == dec[1] == dec[2]):
  print "TRIANGULO EQUILATERO"
elif (dec[0] == dec[1]) or (dec[0] == dec[2]) or (dec[2] == dec[1]):
  print "TRIANGULO ISOSCELES"
  
  
