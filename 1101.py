somam =0
for i in range (10000):
  M, N = map(int,raw_input().split())
  if M <= 0 or N <= 0:
    break
  if (M < N):
    for i in range (M, N+1):
      somam += i
      print "%d" %(i),
  elif (M > N):
    for i in range (N, M+1):
      somam += i
      print "%d" %(i),
  print "Sum=%d" %(somam)
  somam = 0
