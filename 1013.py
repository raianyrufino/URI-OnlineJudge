a,b,c = map(int,raw_input().split())

maiorab= (a+b+abs(a-b))/2
maiorac= (a+c+abs(a-c))/2
maior= (maiorab+maiorac+abs(maiorab-maiorac))/2

print("%d eh o maior" % (maior))s
