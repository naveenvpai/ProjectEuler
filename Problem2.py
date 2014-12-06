def evenFib():
	a = 1
	b = 1
	sum = 0
	while (a+b < 4000000):
		if ((a+b) % 2 == 0):
			sum = sum+a+b
		next = a+b
		a = b
		b = next
	return sum
print(evenFib())

	