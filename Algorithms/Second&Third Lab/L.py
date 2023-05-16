def get_lis_length(arr: list) -> tuple:
    n = len(arr)
    dp = [0] * n
    prev = [-1] * n
    for i in range(n):
        j = 0
        while j < i:
            if arr[j] < arr[i] and dp[j] > dp[i]:
                dp[i] = dp[j]
                prev[i] = j
            j += 1
        dp[i] += 1
    max_index = 0
    for i in range(n):
        if dp[i] > dp[max_index]:
            max_index = i
    result = []
    while max_index != -1:
        result.append(arr[max_index])
        max_index = prev[max_index]
    result.reverse()
    return len(result), result


if __name__ == '__main__':
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(get_lis_length(arr)[0])
    print(" ".join(map(str, get_lis_length(arr)[1])))