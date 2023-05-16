class Stack:
	def __init__(self):
		self.stack = []
		self.min = []
		self.operations = []

	def push(self, x):
		self.stack.append(x)
		if len(self.min) == 0 or x <= self.min[-1]:
			self.min.append(x)

	def pop(self):
		if self.stack[-1] == self.min[-1]:
			self.min.pop()
		self.stack.pop()

	def sort(self):
		temp = Stack()
		while len(self.stack) != 0:
			if len(temp.stack) == 0:
				temp.push(self.stack.pop())
			else:
				if temp.stack[-1] > self.stack[-1]:
					temp.push(self.stack.pop())
				else:
					temp2 = Stack()
					while len(temp.stack) != 0 and temp.stack[-1] < self.stack[-1]:
						temp2.push(temp.stack.pop())
					temp.push(self.stack.pop())
					while len(temp2.stack) != 0:
						temp.push(temp2.stack.pop())
		return temp

	def __str__(self):
		return str(self.stack)



if __name__ == '__main__':
	# my_stack = Stack()
	# n = int(input())
	# a = [int(x) for x in input().split()]
	# for i in range(n):
	# 	my_stack.push(a[i])
	# another = my_stack.sort()
	# print(another)
