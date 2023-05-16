def gcd_n(*numbers: list[int]) -> list[int]:
	it = iter(numbers)
	g = next(it)
	for n in it:
		g = gcd(g, n)
	return g


def gcd(a: int, b: int) -> int:
	while b:
		a, b = b, a % b
	return a


if __name__ == '__main__':
	n = int(input())
	numbers = map(int, input().split())
	print(gcd_n(*numbers))