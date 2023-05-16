n = int(input())
a = [0] * (n + 1)
a[1] = 8
for i in range(2, n + 1):
    a[i] = a[i - 1] * 9 - a[i - 2] * 2
print(a[n] % 10**9)