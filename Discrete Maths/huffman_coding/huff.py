from collections import Counter


class NodeTree(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return self.left, self.right

    def __str__(self):
        return self.left, self.right


def huffman_code_tree(node, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, binString + '0'))
    d.update(huffman_code_tree(r, binString + '1'))
    return d


def make_tree(nodes):
    while len(nodes) > 1:
        (key1, c1) = nodes[-1]
        (key2, c2) = nodes[-2]
        nodes = nodes[:-2]
        node = NodeTree(key1, key2)
        nodes.append((node, c1 + c2))
        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)
    return nodes[0][0]


if __name__ == '__main__':
    s = "abacaba"
    node = dict(Counter(s))
    hash_sorted = sorted(node.items(), key=lambda x: x[1], reverse=True)
    nodes = make_tree(hash_sorted)
    encoding = dict(huffman_code_tree(nodes))
    new = {str(k): str(v) for k,v in encoding.items()}
    result = ""
    for i in range(len(s)):
        result += new[s[i]]
    print(int(result, 2))
