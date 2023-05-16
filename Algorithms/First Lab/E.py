from typing import List


def merge_sort(arr: List[int], l: int, r: int):
    if l < r:
        m = l + (r - l) // 2
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        merge(arr, l, m, r)


def merge(arr: List[int] , l: int, m: int, r: int):
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


def lower_bound(arr: List[int], l: int, r: int, x: int) -> int:
    while l < r:
        m = l + (r - l) // 2
        if arr[m] < x:
            l = m + 1
        else:
            r = m
    return l


def upper_bound(arr: List[int], l: int, r: int, x: int) -> int:
    while l < r:
        m = l + (r - l) // 2
        if arr[m] <= x:
            l = m + 1
        else:
            r = m
    return l


if __name__ == '__main__':
    n = int(input())
    arr = [int(x) for x in input().split()]
    k = int(input())
    queries = [[int(x) for x in input().split()] for _ in range(k)]
    merge_sort(arr, 0, len(arr) - 1)
    for query in queries:
        print(upper_bound(arr, 0, len(arr), query[1]) - lower_bound(arr, 0, len(arr), query[0]), end=' ')