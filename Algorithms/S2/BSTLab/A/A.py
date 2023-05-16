class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
            return

        node = self.root
        while node:
            if val < node.val:
                if node.left is None:
                    node.left = Node(val)
                    return
                node = node.left
            elif val > node.val:
                if node.right is None:
                    node.right = Node(val)
                    return
                node = node.right
            else:
                return

    def delete(self, val):
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
                    node = None
                    return temp
                elif node.right is None:
                    temp = node.left
                    node = None
                    return temp
                temp = find_min_node(node.right)
                node.val = temp.val
                node.right = delete_node(node.right, temp.val)
            return node

        self.root = delete_node(self.root, val)

    def exists(self, val):
        node = self.root
        while node:
            if val < node.val:
                node = node.left
            elif val > node.val:
                node = node.right
            else:
                return True
        return False

    def next(self, val):
        node = self.root
        next_val = None
        while node:
            if node.val > val:
                next_val = node.val
                node = node.left
            else:
                node = node.right
        return next_val

    def prev(self, val):
        node = self.root
        prev_val = None
        while node:
            if node.val < val:
                prev_val = node.val
                node = node.right
            else:
                node = node.left
        return prev_val


if __name__ == '__main__':
    bst = BST()
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