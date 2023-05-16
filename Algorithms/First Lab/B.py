from typing import List


def countSort(arr: List) -> List[int]:
    k = max(arr)
    count = [0 for _ in range(k + 1)]
    result = [0 for _ in range(len(arr))]
    for i in range(len(arr)):
        count[arr[i]] += 1
    p = 0
    for i in range(k + 1):
        for j in range(count[i]):
            result[p] = i
            p += 1
    return result


if __name__ == '__main__':
    n = int(input())
    arr = [int(x) for x in input().split()]
    result = countSort(arr)
    print(*result)