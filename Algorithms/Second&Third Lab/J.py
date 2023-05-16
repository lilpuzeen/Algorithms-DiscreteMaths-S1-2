def grasshooper(n, k, coins):
	dp = [0] * (n + 1)
	dp[0] = 1
	for i in range(1, n + 1):
		for j in range(k):
			if i - coins[j] >= 0:
				dp[i] += dp[i - coins[j]]
	return dp[n]


if __name__ == '__main__':
	n, k = map(int, input().split())
	coins = [int(x) for x in input().split()]
	print(grasshooper(n, k, coins))