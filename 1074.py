n = int(raw_input())

if (n < 10000):
  for i in range (n):
    x = int(raw_input())
    if x > 0 and x %2 == 0:
      print "EVEN POSITIVE"
    elif x > 0 and x%2 == 1:
      print "ODD POSITIVE"
    elif x < 0 and x %2 == 0:
      print "EVEN NEGATIVE"
    elif x <0 and x%2 ==1:
      print "ODD NEGATIVE"
    else:
      print "NULL"
