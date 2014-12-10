
import math
	
def genPrimes(n):
	prime	= [True] * (n+1)
	q = 2
	l = []
	while (q <= n):
		if (prime[q]):
			for j in range(2, n/q+1):
				prime[q*j] = False
		q+=1
	for i in range(2, len(prime)):
		if (prime[i]): l.append(i)
	return l	
	
	
def greatestPrimeFactor(n):
	g = genPrimes(int(math.sqrt(n)))
	for i in g:
		if (n%i == 0): n = n/i
		if n in g : return n
	return 1
	
print greatestPrimeFactor(600851475143)


	
	