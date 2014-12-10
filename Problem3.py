"""
Problem 3:

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

Solution:

Initially tried a brute force solution
- had an isPrime method of O(n) for each factor --> very ineff.
- led to memory error

Decided to use Sieve of Eratosthenes (genPrimes):
- lists all the the prime numbers under sqrt(n)
- for those that are factors, divide n by them
- once n is prime program has found the largest prime factor
- NOTE: the result of genPrimes cannot be a generator b/c the method
 greatestPrimeFactor needs to ref. the list to check if n is prime
"""
import math
	
def genPrimes(n):
	prime	= [True] * (n+1)
	q = 2
	listPrimes = []
	while (q <= n):
		if (prime[q]):
			for j in range(2, n/q+1):
				prime[q*j] = False
		q+=1
	for i in range(2, len(prime)):
		if (prime[i]): listPrimes.append(i)
	return listPrimes
	
	
def greatestPrimeFactor(n):
	g = genPrimes(int(math.sqrt(n)))
	for i in g:
		if (n%i == 0): n = n/i
		if n in g : return n
	return 1
	
print greatestPrimeFactor(600851475143)


	
	