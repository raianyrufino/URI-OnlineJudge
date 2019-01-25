def test_prime(n):
    if (n==1):
        return "%d nao eh primo"%(n)
    elif (n==2):
        return "%d eh primo"%(n);
    else:
        for x in range(2,n):
            if(n % x==0):
                return "%d nao eh primo"%(n)
        return "%d eh primo"%(n)         
        
        
n = int(raw_input())
 
if n >= 1 and n <= 100:
  for i in range(n):
    x = int(raw_input())
    print test_prime(x)
