class DisjointSet:
	def __init__(self, n):
		self.parent = [i for i in range(n)]
		self.rank = [0 for i in range(n)]

	def find(self, x):
		if self.parent[x] == x:
			return x
		self.parent[x] = self.find(self.parent[x])
		return self.parent[x]

	def union(self, x, y):
		x = self.find(x)
		y = self.find(y)
		if x == y:
			return
		if self.rank[x] > self.rank[y]:
			self.parent[y] = x
		else:
			self.parent[x] = y
			if self.rank[x] == self.rank[y]:
				self.rank[y] += 1

	def __str__(self):
		return str(self.parent)


if __name__ == '__main__':
	n = int(input())
	sets = [DisjointSet(n) for i in range(n)]

	while True:
		command = [x for x in input().split()]
		if command[0] == "union":
			sets[int(command[1])].union(int(command[1]), int(command[2]))
		elif command[0] == "get":
			print(sets[int(command[1])].find(command[1]))
		elif command == "exit":
			break
		else:
			print("Unknown command")