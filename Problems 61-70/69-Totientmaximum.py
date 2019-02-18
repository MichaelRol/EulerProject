
def phi(n): 
    result = n  
    p = 2
    while p * p<= n:
        if  n % p == 0: 
            while n % p == 0: 
                n = n // p 
            result = result * (1.0 - (1.0 / (float) (p))) 
        p = p + 1
    if n > 1: 
        result = result * (1.0 - (1.0 / (float)(n))) 
   
    return (int)(result) 

max = 0
value = 0
for n in range(2, 1000000):
    nphin = float(n)/float(phi(n))
    if nphin > max:
        count = 0
        max = nphin
        value = n

print(value)