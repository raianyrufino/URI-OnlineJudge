alcool = 0 
gaso = 0 
diesel = 0
for i in range(10000):
  x = int(raw_input())
  if x == 4:
    break
  elif x == 1:
    alcool += 1 
  elif x == 2:
    gaso += 1 
  elif x == 3:
    diesel += 1
print "MUITO OBRIGADO"
print "Alcool: %d" %(alcool)
print "Gasolina: %d" %(gaso)
print "Diesel: %d" %(diesel)
    
