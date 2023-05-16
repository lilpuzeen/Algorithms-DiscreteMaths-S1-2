from itertools import permutations, product


def choose(n, k):
	if k == 0:
		return 1
	if n <= 0 or k < 0:
		return 0
	return choose(n, k - 1) * (n - k + 1) // k


def arrange(n, k):
	if k == 0:
		return 1
	if n <= 0 or k < 0:
		return 0
	return arrange(n, k - 1) * (n - k + 1)


def permute(n, k):
	if k == 0:
		return 1
	if n <= 0 or k < 0:
		return 0
	return permute(n, k - 1) * n


if __name__ == '__main__':
	# print(choose(8, 3) + choose(7, 3) + choose(6, 3))
	# print(choose(4, 2))
	# print(len(list(permutations("abbbcddeee"))))
	print(choose(52, 13))