A, B, C = map(float,raw_input().split())

if (A+B > C) and (B+C > A) and (C+A >B):
  perimetro = A+B+C
  print("Perimetro:  %.1f" %(perimetro))
else:
  area = (A+B)*C/2
  print("Area: %.1f" %(area))
