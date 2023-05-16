from typing import List


def heapify(arr: List[int], n: int, i: int):
	largest = i
	l = 2 * i + 1
	r = 2 * i + 2

	if l < n and arr[i] < arr[l]:
		largest = l

	if r < n and arr[largest] < arr[r]:
		largest = r

	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i]
		heapify(arr, n, largest)


def insertKey(arr: List[int], key: int):
	n = len(arr)
	arr.append(key)
	i = n - 1
	while i != 0 and arr[i] > arr[(i - 1) // 2]:
		arr[i], arr[(i - 1) // 2] = arr[(i - 1) // 2], arr[i]
		i = (i - 1) // 2


def swap(arr: List[int], i: int, j: int):
	arr[i], arr[j] = arr[j], arr[i]


def extractMax(arr: List[int]):
	n = len(arr)
	while arr[0] < arr[n - 1]:
		swap(arr, 0, n - 1)
		n -= 1
		heapify(arr, n, 0)
	swap(arr, 0, n - 1)
	maxx = arr[n - 1]
	arr.pop(n - 1)
	heapify(arr, n - 1, 0)
	return maxx


if __name__ == '__main__':
	n = int(input())
	queries = [[int(i) for i in input().split()] for _ in range(n)]
	arr = []
	for query in queries:
		if query[0] == 0:
			insertKey(arr, query[1])
		elif query[0] == 1:
			print(extractMax(arr))
