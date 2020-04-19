class Node:
    def __init__(self, left, weight, right=None):
        self.left = left
        self.weight = weight
        self.right = right

    def __str__(self, h=1):
        if self.right is None:
            return '#' + str(self.weight) + ' ' + self.left

        res = '#' + str(self.weight) + '\n'
        res += ' ' * h + '0 -> ' + self.left.__str__(h + 1) + '\n'
        res += ' ' * h + '1 -> ' + self.right.__str__(h + 1)
        return res


class HuffmanTree:
    def __init__(self, letter_counts):
        nodes = []
        for a, weight in letter_counts.items():
            nodes.append(Node(a, weight))
        internal_nodes = []
        leafs = sorted(nodes, key=lambda n: n.weight)
        while len(leafs) + len(internal_nodes) > 1:
            head = []
            if len(leafs) >= 2:
                head += leafs[:2]
            elif len(leafs) == 1:
                head += leafs[:1]
            if len(internal_nodes) >= 2:
                head += internal_nodes[:2]
            elif len(internal_nodes) == 1:
                head += internal_nodes[:1]
            element_1, element_2 = sorted(head, key=lambda n: n.weight)[:2]
            internal_nodes.append(Node(element_1,
                                       element_1.weight + element_2.weight,
                                       element_2))
            if len(leafs) > 0 and element_1 == leafs[0]:
                leafs = leafs[1:]
            else:
                internal_nodes = internal_nodes[1:]
            if len(leafs) > 0 and element_2 == leafs[0]:
                leafs = leafs[1:]
            else:
                internal_nodes = internal_nodes[1:]
        # return internal_nodes[0]
        self.root = internal_nodes[0]

    def get_root(self):
        return self.root