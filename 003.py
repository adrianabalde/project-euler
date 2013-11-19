"""
Largest prime factor
--------------------
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

def primes(n):
	factor = []
	d = 2
	while n > 1:
		while n % d == 0:
			factor.append(d)
			n /= d
		d += 1
	return factor

print max(primes(600851475143))

#Answer: 6857