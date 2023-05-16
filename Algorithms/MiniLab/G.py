def lcm(a: int, b: int) -> int:
	return a * b // gcd(a, b)


def gcd(a: int, b: int) -> int:
	while b:
		a, b = b, a % b
	return a


if __name__ == '__main__':
	n, k = map(int, input().split())
	print(lcm(n, k))