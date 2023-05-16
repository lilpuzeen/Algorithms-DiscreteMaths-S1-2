def get_levenstein_distance(first: str, second: str) -> int:
	n = len(first)
	m = len(second)
	dp = [[0] * (m + 1) for i in range(n + 1)]
	for i in range(n + 1):
		for j in range(m + 1):
			if i == 0:
				dp[i][j] = j
			elif j == 0:
				dp[i][j] = i
			elif first[i - 1] == second[j - 1]:
				dp[i][j] = dp[i - 1][j - 1]
			else:
				dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
	return dp[n][m]


if __name__ == '__main__':
	first = input()
	second = input()
	print(get_levenstein_distance(first, second))