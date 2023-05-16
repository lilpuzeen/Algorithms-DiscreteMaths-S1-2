n, x, y, a0 = map(int, input().split())
m, z, t, b0 = map(int, input().split())

pref = [a0]
for i in range(1, n):
    a0 = (x*a0 + y) % 2**16
    pref.append((pref[i - 1]) + a0)


s = 0
previous_b = b0
for i in range(m):
	next_b = (z * previous_b + t) % 2**30
	l, r = min(previous_b % n, next_b % n), max(previous_b % n, next_b % n)
	if l == 0:
		s += pref[r]
	else:
		s += pref[r] - pref[l - 1]
	previous_b = (z * next_b + t) % 2**30
print(s)
