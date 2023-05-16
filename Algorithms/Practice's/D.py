def get_horse_from_top_bottom(n: int, m: int) -> int:
	dp = [[0] * m for _ in range(n)]
	dp[0][0] = 1
	for i in range(n):
		for j in range(m):
			if i + 2 < n and j + 1 < m:
				dp[i + 2][j + 1] += dp[i][j]
			if i + 1 < n and j + 2 < m:
				dp[i + 1][j + 2] += dp[i][j]
	return dp[-1][-1]
	# return dp[n - 1][m - 1]


if __name__ == '__main__':
	n, m = map(int, input().split())
	print(get_horse_from_top_bottom(n, m))
