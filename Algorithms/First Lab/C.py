from typing import List


def merge(arr: List[int], extra: List[int], l: int, m: int, r: int) -> int:
	inversion_count = 0
	k = i = l
	j = m + 1

	while i <= m and j <= r:
		if arr[i] <= arr[j]:
			extra[k] = arr[i]
			i += 1
		else:
			extra[k] = arr[j]
			j += 1
			inversion_count += (m + 1 - i)
		k += 1

	while i <= m:
		extra[k] = arr[i]
		k += 1
		i += 1

	for i in range(l, r + 1):
		arr[i] = extra[i]

	return inversion_count


def mergesort(arr: List[int], extra: List[int], l: int, r: int) -> int:
	if r <= l:
		return 0

	mid = l + (r - l) // 2
	inversion_count = 0

	inversion_count += mergesort(arr, extra, l, mid)
	inversion_count += mergesort(arr, extra, mid + 1, r)
	inversion_count += merge(arr, extra, l, mid, r)

	return inversion_count


if __name__ == '__main__':
	n = int(input())
	arr = [int(x) for x in input().split()]
	extra = arr.copy()
	print(mergesort(arr, extra, 0, len(arr) - 1))
