from math import factorial


def median(a: int, b: int, c: int):
	arr = [a, b, c]
	return int(arr.count(1) >= 2)


def combinations(n: int, k: int) -> float:
	return (factorial(n)) / (factorial(k) * factorial(n - k))


print(combinations(10, 6))