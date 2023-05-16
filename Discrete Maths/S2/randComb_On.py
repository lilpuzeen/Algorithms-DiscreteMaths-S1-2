from typing import List
from randPerm import random_permutation


def randComb(array: List[int], n: int, k: int) -> List[int]:
	a = [0]*n
	answer = []
	for i in range(n):
		if i <= k:
			a[i] = 1
		else:
			a[i] = 0
	a = random_permutation(a)
	for i in range(n):
		if a[i] == 1:
			answer.append(array[i])
	return answer


if __name__ == '__main__':
    print(randComb([1, 3, 5, 6, 8], 5, 2))