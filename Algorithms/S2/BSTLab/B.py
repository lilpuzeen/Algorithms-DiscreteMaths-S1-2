class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		self.height = 1


class AVLTree:
	def __init__(self):
		self.root = None

	def insert(self, val):
		def get_height(node):
			if node is None:
				return 0
			return node.height

		def get_balance(node):
			if node is None:
				return 0
			return get_height(node.left) - get_height(node.right)

		def rotate_left(node):
			right_child = node.right
			node.right = right_child.left
			right_child.left = node
			node.height = max(get_height(node.left), get_height(node.right)) + 1
			right_child.height = max(get_height(right_child.left), get_height(right_child.right)) + 1
			return right_child

		def rotate_right(node):
			left_child = node.left
			node.left = left_child.right
			left_child.right = node
			node.height = max(get_height(node.left), get_height(node.right)) + 1
			left_child.height = max(get_height(left_child.left), get_height(left_child.right)) + 1
			return left_child

		def insert_node(node, val):
			if node is None:
				return Node(val)

			if val < node.val:
				node.left = insert_node(node.left, val)
			elif val > node.val:
				node.right = insert_node(node.right, val)
			else:
				return node

			node.height = max(get_height(node.left), get_height(node.right)) + 1
			balance = get_balance(node)

			if balance > 1 and val < node.left.val:
				return rotate_right(node)

			if balance < -1 and val > node.right.val:
				return rotate_left(node)

			if balance > 1 and val > node.left.val:
				node.left = rotate_left(node.left)
				return rotate_right(node)

			if balance < -1 and val < node.right.val:
				node.right = rotate_right(node.right)
				return rotate_left(node)

			return node

		self.root = insert_node(self.root, val)

	def delete(self, val):
		def get_height(node):
			if node is None:
				return 0
			return node.height

		def get_balance(node):
			if node is None:
				return 0
			return get_height(node.left) - get_height(node.right)

		def rotate_left(node):
			right_child = node.right
			node.right = right_child.left
			right_child.left = node
			node.height = max(get_height(node.left), get_height(node.right)) + 1
			right_child.height = max(get_height(right_child.left), get_height(right_child.right)) + 1
			return right_child

		def rotate_right(node):
			left_child = node.left
			node.left = left_child.right
			left_child.right = node
			node.height = max(get_height(node.left), get_height(node.right)) + 1
			left_child.height = max(get_height(left_child.left), get_height(left_child.right)) + 1
			return left_child

		def find_min_node(node):
			while node.left:
				node = node.left
			return node

		def delete_node(node, val):
			if node is None:
				return node

			if val < node.val:
				node.left = delete_node(node.left, val)

			elif val > node.val:
				node.right = delete_node(node.right, val)

			else:
				if node.left is None:
					temp = node.right
					del node
					return temp

				elif node.right is None:
					temp = node.left
					del node
					return temp

				temp = find_min_node(node.right)
				node.val = temp.val
				node.right = delete_node(node.right, temp.val)

			if node is None:
				return node

			node.height = max(get_height(node.left), get_height(node.right)) + 1
			balance = get_balance(node)

			if balance > 1 and get_balance(node.left) >= 0:
				return rotate_right(node)

			if balance < -1 and get_balance(node.right) <= 0:
				return rotate_left(node)

			if balance > 1 and get_balance(node.left) < 0:
				node.left = rotate_left(node.left)
				return rotate_right(node)

			if balance < -1 and get_balance(node.right) > 0:
				node.right = rotate_right(node.right)
				return rotate_left(node)

			return node

		self.root = delete_node(self.root, val)

	def exists(self, val):
		def search_node(node, val):
			if node is None:
				return False

			if node.val == val:
				return True

			if node.val < val:
				return search_node(node.right, val)

			return search_node(node.left, val)

		return search_node(self.root, val)

	def next(self, val):
		def find_next_node(node, val):
			if node is None:
				return None

			if node.val <= val:
				return find_next_node(node.right, val)

			left_node = find_next_node(node.left, val)

			if left_node is not None:
				return left_node

			return node.val

		next_node = find_next_node(self.root, val)

		if next_node is None:
			return None

		return next_node

	def prev(self, val):
		def find_prev_node(node, val):
			if node is None:
				return None

			if node.val >= val:
				return find_prev_node(node.left, val)

			right_node = find_prev_node(node.right, val)

			if right_node is not None:
				return right_node

			return node.val

		prev_node = find_prev_node(self.root, val)

		if prev_node is None:
			return None

		return prev_node


if __name__ == '__main__':
	bst = AVLTree()
	while True:
		try:
			command = input().split()
			if command[0] == 'insert':
				bst.insert(int(command[1]))
			elif command[0] == 'delete':
				bst.delete(int(command[1]))
			elif command[0] == 'exists':
				print('true' if bst.exists(int(command[1])) else 'false')
			elif command[0] == 'next':
				print(bst.next(int(command[1])) or 'none')
			elif command[0] == 'prev':
				print(bst.prev(int(command[1])) or 'none')
		except EOFError:
			break
