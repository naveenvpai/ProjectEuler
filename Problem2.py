"""
Problem 2:

Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed 
four million, find the sum of the even-valued terms.

Solution:

Iteratively create fibonacci sequence, adding even elements to sum (n%2 == 0)
- NOTE: An iterative process is more efficient than recursive in this situation because 
a recursive fibonacci sequence overlaps (tree recursion --> ineff.)

MISTAKE: struggled with syntax (remember to carefully examine the lines above an error)
"""

def evenFib():
	a = 1
	b = 1
	sum = 0
	while (a+b < 4000000):
		if ((a+b) % 2 == 0): sum = sum+a+b
		next = a+b
		a = b
		b = next
	return sum
print(evenFib())

	