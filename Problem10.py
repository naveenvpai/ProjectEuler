"""
Problem 10:

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

Solution:
Using the Sieve of Eratosthenes created in Problem 3,
I created a list of all of the primes under 2,000,000
and found its sum.
"""

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

n = 2000000
l = genPrimes(n)
sum = 0

for prime in l:
	sum += prime

print(sum)