from functools import lru_cache
import random
import math


@lru_cache(maxsize=None)
def random_variable(n: int, E: float, D: float) -> list:
	random_list = [random.random() for i in range(int(n))]
	random_list.sort()
	random_variable_list = [math.sqrt(12 * D) * random_list[i] + E for i in range(int(n))]
	return random_variable_list


if __name__ == '__main__':
	n, E, D = 9, 11.8827, 56.8397
	while True:
		rv = random_variable(n, E, D)
		expected_value = sum(rv) / 100
		variance = (sum([i**2 for i in rv]) / 100) - expected_value**2
		if (expected_value - E) < 0.0001 and (variance - D) < 0.0001:
			print(rv)
			break