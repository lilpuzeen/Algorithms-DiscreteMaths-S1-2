from typing import List


def binary_search(target: int, arr: List[int]) -> int:
    left = -1
    right = len(arr)

    while left + 1 < right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] < target:
            left = mid
        else:
            right = mid

    if left == -1:
        return arr[right]
    elif right == len(arr):
        return arr[left]

    if target - arr[left] <= arr[right] - target:
        return arr[left]

    return arr[right]


if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = [int(x) for x in input().split()]
    queries = [int(x) for x in input().split()]
    for q in queries:
        result = binary_search(q, arr)
        print(result)
