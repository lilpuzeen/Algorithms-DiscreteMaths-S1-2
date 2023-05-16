from functools import lru_cache


@lru_cache(None)
class Stack:
	def __init__(self):
		self.stack = []
		self.min = []

	def push(self, x):
		self.stack.append(x)
		if len(self.min) == 0 or x <= self.min[-1]:
			self.min.append(x)

	def pop(self):
		if self.stack[-1] == self.min[-1]:
			self.min.pop()
		self.stack.pop()

	def getMin(self):
		return self.min[-1]


if __name__ == '__main__':
	my_stack = Stack()
	n = int(input())
	for i in range(n):
		command = [int(x) for x in input().split()]
		if command[0] == 1:
			my_stack.push(int(command[1]))
		elif command[0] == 2:
			my_stack.pop()
		elif command[0] == 3:
			print(my_stack.getMin())
