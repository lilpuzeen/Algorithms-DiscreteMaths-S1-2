import math


def ternary_search(l: float, r: float, f, eps=1e-9):
	while r - l > eps:
		a = (l*2 + r) / 3
		b = (l + r*2) / 3
		if f(a) < f(b):
			r = b
		else:
			l = a
	return (l + r) / 2


def time_for_field(x: float, a: float, v: float):
	return math.sqrt((1 - a) ** 2 + x ** 2) / v


def time_for_forest(x: float, b: float, v: float):
	return math.sqrt(b ** 2 + (1 - x) ** 2) / v


if __name__ == '__main__':
	v_field, v_forest = map(float, input().split())
	a = float(input())
	print(ternary_search(0, 1, lambda x: time_for_field(x, a, v_field) + time_for_forest(x, a, v_forest)))
