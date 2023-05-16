def gcd(a, b):
	while b:
		a, b = b, a % b
	return a


def add_fraction(a, b, c, d):
	ad = a * d
	bc = b * c
	bd = b * d
	numerator = ad + bc
	denominator = bd
	gcd_ = gcd(numerator, denominator)
	numerator = numerator // gcd_
	denominator = denominator // gcd_
	return numerator, denominator


if __name__ == '__main__':
	a, b, c, d = map(int, input().split())
	numerator, denominator = add_fraction(a, b, c, d)
	print(numerator, denominator)