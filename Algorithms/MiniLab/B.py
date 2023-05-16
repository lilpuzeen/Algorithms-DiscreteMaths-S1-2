def p(x: int) -> bool:
	return x > 1 and all(x % i for i in range(2, int(x ** 0.5) + 1))


if __name__ == '__main__':
    a, b = map(int, input().split())
    primes = [x for x in range(a, b + 1) if p(x)]
    print(*primes)
