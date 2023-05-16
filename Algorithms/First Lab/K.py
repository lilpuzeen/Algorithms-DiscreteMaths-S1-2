def binsearch(arr: list[int], k: int) -> int:
	l = -1
	r = sum(arr)
	while (r - l) > 1:
		m = (l + r) // 2
		if cuts_count(arr, m, k-1):
			r = m
		else:
			l = m
	return r


def cuts_count(arr: list[int], maxx: int, cuts_count: int) -> bool:
	tmp_sum = 0
	cuts = 0
	for i in range(len(arr)):
		if arr[i] > maxx:
			return False
		tmp_sum += arr[i]
		if tmp_sum > maxx:
			cuts += 1
			tmp_sum = arr[i]

	return cuts <= cuts_count


if __name__ == '__main__':
	n, k = map(int, input().split())
	arr = [int(_) for _ in input().split()]
	print(binsearch(arr, k))

