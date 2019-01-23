n = int(raw_input())

for i in range (n):
  x, y, z = map(float, raw_input().split())
  media = ((x*2) + (y*3) + (z*5))/ 10
  print "%.1f" %(media)
