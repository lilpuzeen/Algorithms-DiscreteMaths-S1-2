if __name__ == '__main__':
    n = int(input())
    m = list(map(int, input().split()))

    s = sum(m)

    if s % 2 == 1:
        print('NO')
    else:
        s //= 2
        dp = [False] * (s + 1)
        dp[0] = True
        for i in range(n):
            for j in range(s, m[i] - 1, -1):
                dp[j] = dp[j] or dp[j - m[i]]
        print('YES' if dp[s] else 'NO')