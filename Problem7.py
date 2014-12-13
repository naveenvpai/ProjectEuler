"""
Problem 7:

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

Solution:

- Generate primes up to a number n using Sieve of Eratosthenes
- Estimate the nth prime to be nlog(n) by Prime Number Theorem
(http://en.wikipedia.org/wiki/Prime_number_theorem)
"""

import numpy

def genPrimes(n):
	isPrime		= [True] * (n+1)
	listPrime	= []
	q			= 2
	while q <= n:
		if isPrime[q]:
			listPrime.append(q)
			for j in range(2, n/q+1):
				isPrime[q*j] = False
		q+=1
	return listPrime

def genThePrime(n):
    limit = int( ( n * (numpy.log(n)) ) *10)
    return genPrimes(limit)[n-1];

print(genThePrime(10001))

	
