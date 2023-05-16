def factorize(n: int):
	i = 2
	while i * i <= n:
		if n % i:
			i += 1
		else:
			n //= i
			print(i, end=" ")
	print(n)


if __name__ == '__main__':
	n = int(input())
	for i in range(n):
		x = int(input())
		factorize(x)