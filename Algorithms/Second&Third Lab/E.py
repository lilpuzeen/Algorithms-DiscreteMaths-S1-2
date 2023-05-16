def postfix_calculate(expression: str) -> int:
	stack = []
	split_expression = expression.split()
	for char in split_expression:
		if char.isdigit():
			stack.append(int(char))
		else:
			a = stack.pop()
			b = stack.pop()
			if char == '+':
				stack.append(b + a)
			elif char == '-':
				stack.append(b - a)
			elif char == '*':
				stack.append(b * a)
	return stack.pop()


if __name__ == '__main__':
    expression = input()
    print(postfix_calculate(expression))
