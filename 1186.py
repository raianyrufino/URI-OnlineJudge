O = raw_input()
soma = 0

for i in range(12):
  for j in range(12):
    a = float(raw_input())
    if ( ( i + j + 1 ) > 12):
      soma = soma+a

if O=="S":
  print("%.1f" %soma)
else:
  print("%.1f" %(soma / 66.0))
