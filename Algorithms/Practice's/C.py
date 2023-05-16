def get_min_operations(n: int) -> tuple:
	dp = [0] * (n + 1)
	for i in range(2, n + 1):
		dp[i] = dp[i - 1] + 1
		if i % 2 == 0:
			dp[i] = min(dp[i], dp[i // 2] + 1)
		if i % 3 == 0:
			dp[i] = min(dp[i], dp[i // 3] + 1)

	seq = []
	while n > 1:
		seq.append(n)
		if dp[n - 1] == dp[n] - 1:
			n = n - 1
		elif n % 2 == 0 and dp[n // 2] == dp[n] - 1:
			n = n // 2
		elif n % 3 == 0 and dp[n // 3] == dp[n] - 1:
			n = n // 3
	seq.append(1)
	return dp[-1], seq[::-1]


if __name__ == '__main__':
	n = int(input())
	quantity, operations = get_min_operations(n)
	print(quantity)
	print(*operations)
