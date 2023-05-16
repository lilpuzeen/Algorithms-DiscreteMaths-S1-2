import random
from typing import List


def random_permutation(perm: List[int]) -> List[int]:
	n = len(perm) - 1
	for i in range(n, 0, -1):
		j = random.randint(1, i)
		perm[i], perm[j] = perm[j], perm[i]
	return perm


if __name__ == '__main__':
    print(random_permutation([1, 5, 3, 7, 9, 6]))
