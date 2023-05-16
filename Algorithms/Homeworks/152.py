# from functools import lru_cache
#
#
# @lru_cache(None)
# def f(start: int, stop: int, step=0) -> int:
# 	if start > stop:
# 		return 10 ** 8
# 	if start == stop:
# 		return step
# 	else:
# 		return min(f(start + 1, stop, step + 1),
# 		           f(start * 2, stop, step + 1),
# 		           f(start * 3, stop, step + 1))
#
#
# if __name__ == '__main__':
# 	n = int(input())
# 	print(f(1, n))


n = int(input())
dp = [0] * n
dp[0] = 1
for i in range(1, len(dp)):
	if i+1 <= n:
		dp[i+1] += dp[i]
	if i*2 <= n:
		dp[i*2] += dp[i]
	if i*3 <= n:
		dp[i*3] += dp[i]