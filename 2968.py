x, y = map(int,raw_input().split())
 
x = x * y
 
for i in range(1, 10):
	por = x / 10.0 * i
	if por != int(por) : 
		por = int(por) +  1	
	print int(por),