x = int(raw_input())

for i in range (x*4):
  if((i+1) % 4 == 0):
    print "PUM"
  else:
    print i+1,
