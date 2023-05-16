def Knuth_Morris_Pratt(T, P):
	n = len(T)
	m = len(P)
	prefix = Prefix (P)
	q = 0
	for i in range(n):
		while q > 0 and P[q] != T[i]:
			q = prefix[q]
		if P[q] == T[i]:
			q = q + 1
		if q == m:
			print(i - m + 1)
			q = prefix[q]


def Prefix(P):
	m = len(P)
	prefix = [0] * (m + 1)
	prefix[0] = -1
	k = -1
	for q in range(1, m + 1):
		while k > -1 and P[k] != P[q - 1]:
			k = prefix[k]
		k = k + 1
		prefix[q] = k
	return prefix


if __name__ == '__main__':
	T = input()
	P = input()
	Knuth_Morris_Pratt(T, P)