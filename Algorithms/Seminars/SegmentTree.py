from functools import total_ordering


class SegmentTree:
	def __init__(self, n, op, e):
		self.n = n
		self.op = op
		self.e = e
		self.data = [e] * (2 * n)

	def build(self, arr):
		for i in range(self.n):
			self.data[i + self.n] = arr[i]
		for i in range(self.n - 1, 0, -1):
			self.data[i] = self.op(self.data[i << 1], self.data[i << 1 | 1])

	def update(self, p, val):
		p += self.n
		self.data[p] = val
		while p > 1:
			self.data[p >> 1] = self.op(self.data[p], self.data[p ^ 1])
			p >>= 1

	def query(self, l, r):
		res = self.e
		l += self.n
		r += self.n
		while l < r:
			if l & 1:
				res = self.op(res, self.data[l])
				l += 1
			if r & 1:
				res = self.op(res, self.data[r - 1])
			l >>= 1
			r >>= 1
		return res

	def __str__(self):
		return str(self.data)

	def __repr__(self):
		return str(self.data)

	def __getitem__(self, item):
		return self.data[item]

	def __setitem__(self, key, value):
		self.data[key] = value

	def __len__(self):
		return len(self.data)

	def __iter__(self):
		return iter(self.data)

	def __reversed__(self):
		return reversed(self.data)

	def __contains__(self, item):
		return item in self.data

	@total_ordering
	def __lt__(self, other):
		return self.data < other.data


st = SegmentTree(10, lambda x, y: x + y, 0)
st.build([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(st)
st.update(2, 10)
print(st)
print(st.query(2, 5))
print(st.query(0, 10))
print(st.query(0, 1))
print(st.query(9, 10))
print(st.query(0, 2))
print(st.query(8, 10))
print(st.query(0, 3))
print(st.query(7, 10))
print(st.query(0, 4))
print(st.query(6, 10))
print(st.query(0, 5))
print(st.query(5, 10))
print(st.query(0, 6))
print(st.query(4, 10))
print(st.query(0, 7))
print(st.query(3, 10))
print(st.query(0, 8))
print(st.query(2, 10))
print(st.query(0, 9))
print(st.query(1, 10))
print(st.query(0, 10))

