class SegmentTree:
	def __init__(self, a):
		self.n = len(a)
		self.tree = [0] * 4 * self.n
		self.lazy = [None] * 4 * self.n

		def build(v, l, r):
			if l == r:
				self.tree[v] = a[l]
			else:
				m = (l + r) // 2
				build(v * 2, l, m)
				build(v * 2 + 1, m + 1, r)
				self.tree[v] = self.tree[v * 2] + self.tree[v * 2 + 1]

		build(1, 0, self.n - 1)

	def push(self, v, l, r):
		if self.lazy[v] is not None:
			self.tree[v] = (r - l + 1) * self.lazy[v]
			if l != r:
				self.lazy[v * 2] = self.lazy[v]
				self.lazy[v * 2 + 1] = self.lazy[v]
			self.lazy[v] = None

	def set(self, l, r, x):
		def update(v, l, r):
			self.push(v, l, r)
			if l > r or l > qr or r < ql:
				return
			if l >= ql and r <= qr:
				self.tree[v] = (r - l + 1) * x
				if l != r:
					self.lazy[v * 2] = x
					self.lazy[v * 2 + 1] = x
			else:
				m = (l + r) // 2
				update(v * 2, l, m)
				update(v * 2 + 1, m + 1, r)
				self.tree[v] = self.tree[v * 2] + self.tree[v * 2 + 1]

		ql, qr = l, r
		update(1, 0, self.n - 1)

	def sum(self, l, r):
		def query(v, l, r):
			self.push(v, l, r)
			if l > r or l > qr or r < ql:
				return 0
			if l >= ql and r <= qr:
				return self.tree[v]
			m = (l + r) // 2
			return query(v * 2, l, m) + query(v * 2 + 1, m + 1, r)

		ql, qr = l, r
		return query(1, 0, self.n - 1)

	def min(self, l, r):
		def query(v, l, r):
			self.push(v, l, r)
			if l > r or l > qr or r < ql:
				return 0
			if l >= ql and r <= qr:
				return self.tree[v]
			m = (l + r) // 2
			return min(query(v * 2, l, m), query(v * 2 + 1, m + 1, r))

		ql, qr = l, r
		return query(1, 0, self.n - 1)


if __name__ == '__main__':
    n = int(input())
    arr = [int(x) for x in input().split()]
    st = SegmentTree(arr)
    while (command := input()) is not None:
        commands = command.split()
        if commands[0] == "min":
            print(st.min(int(commands[1]), int(commands[2])))
        elif commands[0] == "set":
            st.set(int(commands[1]), int(commands[1]), int(commands[2]))

