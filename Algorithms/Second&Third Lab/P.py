def longest_valid_parentheses(s):
    n = len(s)
    if n == 0:
        return 0
    dp = [0] * n
    for i in range(1, n):
        if s[i] == ')' and s[i - 1] == '(':
            dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
        if s[i] == ')' and s[i - 1] == ')' and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
            dp[i] = dp[i - 1] + ((dp[i - dp[i - 1] - 2] if i - dp[i - 1] >= 2 else 0) + 2)
    return max(dp)


if __name__ == '__main__':
	print(longest_valid_parentheses(input()))