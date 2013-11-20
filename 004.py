def is_palindrome(n):
	digits = len(str(n))
	if digits % 2 == 0:
		digits /= 2
	else:
		digits = digits - 1
	list_n = map(int, str(n))
	for i in range(0,digits):
		if list_n[i] != list_n[len(str(n))-i-1]:
			return False
	return True

palindromes = []

for x in range(1,1000):
	for y in range(1,1000):
		product = x * y
		if is_palindrome(product):
			palindromes.append(product)

print max(palindromes)