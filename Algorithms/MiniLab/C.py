import math


def prime(x: int) -> bool:
	for i in range(2, int(math.sqrt(x) + 1)):
		if x % i == 0:
			return False
	return True


if __name__ == '__main__':
	n = int(input())
	for i in range(n):
		x = int(input())
		print("YES" if prime(x) else "NO")