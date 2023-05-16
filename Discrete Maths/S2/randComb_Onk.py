import random
from typing import List


def randComb(array: List[int], n: int, k: int) -> List[int]:
	res = [0]*k
	exist = [True]*n
	for i in range(k):
		r = random.randint(1, (n - i + 1))
		cur = 0
		for j in range(n):
			if exist[j]:
				cur += 1
				if cur == r:
					res[i] = array[j]
					exist[j] = False
	return sorted(res)


if __name__ == '__main__':
    print(randComb([1, 3, 5, 6, 8], 5, 2))