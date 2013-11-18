a = 1
b = 0
s = 0

while a < 4000000:
	a, b = a+b, a
	if a % 2 == 0:
		s += a

print s