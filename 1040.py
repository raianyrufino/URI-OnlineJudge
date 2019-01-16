A, B, C, D = map(float,raw_input().split())


media = ((A*2) + (B*3) + (C*4) + (D*1))/10

if media >= 7.0:
  print("Media: %.1f" %(media))
  print("Aluno aprovado.")
elif media < 5.0:
  print("Media: %.1f" %(media))
  print("Aluno reprovado.")
else:
  print("Media: %.1f" %(media))
  print("Aluno em exame.")
  exame = float(raw_input())
  print("Nota do exame: %.1f" %(exame))
  mediafinal = (media + exame)/2
  if mediafinal >= 5.0:
    print("Aluno aprovado.")
    print("Media final: %.1f" %(mediafinal))
  else:
    print("Aluno reprovado")
    print("Media final: %.1f" %(mediafinal))
