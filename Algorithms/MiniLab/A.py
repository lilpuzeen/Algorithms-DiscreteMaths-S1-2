# given integer n, return True if n has 4 prime factors, otherwise return False

def p(x: int) -> bool:
	return x > 1 and all(x % i for i in range(2, int(x ** 0.5) + 1))


def is_unusual(n: int) -> bool:
	primes = [x for x in range(2, n + 1) if p(x)]
	d = primes[0]
	i = 0
	factors = 0
	while n > 1:
		if n % d == 0:
			factors += 1
			n //= d
		else:
			i += 1
			d = primes[i]
	return factors == 4


if __name__ == '__main__':
	# n = int(input())
	# print(is_unusual(n))
	n = int(input())
	arr = [((-1)**i)*i for i in range(1, n+1)]
	print(sum(arr))