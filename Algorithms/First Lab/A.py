def merge_sort(arr, l, r):
	if l < r:
		m = l + (r - l) // 2
		merge_sort(arr, l, m)
		merge_sort(arr, m + 1, r)
		merge(arr, l, m, r)


def merge(arr , l, m, r):
	range1 = m - l + 1
	range2 = r - m

	leftarr = [0] * range1
	rightarr = [0] * range2

	for i in range(0, range1):
		leftarr[i] = arr[l + i]

	for j in range(0, range2):
		rightarr[j] = arr[m + 1 + j]

	i = 0
	j = 0
	k = l

	while i < range1 and j < range2:
		if leftarr[i] <= rightarr[j]:
			arr[k] = leftarr[i]
			i += 1
		else:
			arr[k] = rightarr[j]
			j += 1
		k += 1

	while i < range1:
		arr[k] = leftarr[i]
		i += 1
		k += 1

	while j < range2:
		arr[k] = rightarr[j]
		j += 1
		k += 1


if __name__ == '__main__':
	n = int(input())
	arr = [int(x) for x in input().split()]
	merge_sort(arr, 0, n - 1)
	print(*arr)