def count_for_first_copy(x: int, y: int) -> int:
	return min(x, y)


def binsearch(l: int, r: int, x: int, y: int, n: int) -> int:
	if r - l <= 1:
		return r

	mid = l + (r - l) // 2

	if (mid // x) + (mid // y) < n:
		return binsearch(mid, r, x, y, n)
	else:
		return binsearch(l, mid, x, y, n)


if __name__ == '__main__':
	n, x, y = map(int, input().split())
	print(binsearch(-1, 10 ** 9, x, y, n - 1) + count_for_first_copy(x, y))

