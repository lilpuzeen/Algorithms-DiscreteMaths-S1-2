class Queue:
	def __init__(self):
		self.items = []

	def enqueue(self, x: str):
		self.items.append(x)

	def delete_last(self):
		self.items.pop()

	def delete_first(self):
		self.items.pop(0)

	def get_index(self, i: str):
		return len(self.items[:self.items.index(i)])

	def front(self):
		return self.items[-1]


if __name__ == '__main__':
	my_queue = Queue()
	n = int(input())
	for i in range(n):
		command = [int(x) for x in input().split()]
		if command[0] == 1:
			my_queue.enqueue(str(command[1]))
		elif command[0] == 2:
			my_queue.delete_first()
		elif command[0] == 3:
			my_queue.delete_last()
		elif command[0] == 4:
			print(my_queue.get_index(str(command[1])))
		elif command[0] == 5:
			print(my_queue.front())
