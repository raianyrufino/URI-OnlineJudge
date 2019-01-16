A, B, C = map(float,raw_input().split())

delta = ((B*B) -(4*A*C))
  


if (delta < 0) or (A == 0):
  print("Impossivel calcular")
  
else:
  raiz = (delta)**0.5
  raizum = (0-B + raiz) /(2*A)
  raizdois = (0-B - raiz) /(2*A)
  print("R1 = %.5f" %(raizum))
  print("R2 = %.5f" %(raizdois))
