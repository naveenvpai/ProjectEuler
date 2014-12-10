def primeFactors(n):
	l = []
	for i in range (2, n):
		while(n%i == 0):
			l.append(i)
			n = n/i
		i+=1
	if (n!=1): l.append(n)
	return l



def isPrime(n):
	if (n==1): return False;
	for i in range(2, n/2):
		if (n%i == 0):return False
	return True