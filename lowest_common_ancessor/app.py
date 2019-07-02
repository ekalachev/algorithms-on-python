class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)

    # Overriding the equality operator.
    # This will be used for testing your solution.
    def __eq__(self, other):
        if type(other) is type(self):
            return self.value == other.value
        return False


def lca(root, j, k):
    j_path = path_to_x(root, j)
    k_path = path_to_x(root, k)

    if j_path is None or k_path is None:
        return None

    result = None
    while len(j_path) > 0 and len(k_path) > 0:
        j_pop = j_path.pop()
        k_pop = k_path.pop()
        if j_pop == k_pop:
            result = j_pop
        else:
            break

    return result


def path_to_x(node, x):
    if node is None:
        return None
    if node.value == x:
        return [node.value]

    left_path = path_to_x(node.left, x)
    if left_path is not None:
        left_path.append(node.value)
        return left_path

    right_path = path_to_x(node.right, x)
    if right_path is not None:
        right_path.append(node.value)
        return right_path

    return None


# A function for creating a tree.
# Input:
# - mapping: a node-to-node mapping that shows how the tree should be constructed
# - head_value: the value that will be used for the head ndoe
# Output:
# - The head node of the resulting tree
def create_tree(mapping, head_value):
    head = Node(head_value)
    nodes = {head_value: head}
    for key, value in mapping.items():
        nodes[value[0]] = Node(value[0])
        nodes[value[1]] = Node(value[1])
    for key, value in mapping.items():
        nodes[key].left = nodes[value[0]]
        nodes[key].right = nodes[value[1]]
    return head


def test():
    # The mapping we're going to use for constructing a tree.
    # {0: [1, 2]} means that 0's left child is 1, and its right
    # child is 2.
    mapping1 = {0: [1, 2], 1: [3, 4], 2: [5, 6]}
    head1 = create_tree(mapping1, 0)
    # This tree is:
    # head1 = 0
    #        / \
    #       1   2
    #      /\   /\
    #     3  4 5  6

    mapping2 = {5: [1, 4], 1: [3, 8], 4: [9, 2], 3: [6, 7]}
    head2 = create_tree(mapping2, 5)
    # This tree is:
    #  head2 = 5
    #        /   \
    #       1     4
    #      /\    / \
    #     3  8  9  2
    #    /\
    #   6  7

    assert lca(head1, 1, 5) == 0
    assert lca(head1, 3, 1) == 1
    assert lca(head1, 1, 4) == 1
    assert lca(head1, 0, 5) == 0
    assert lca(head2, 4, 7) == 5
    assert lca(head2, 3, 3) == 3
    assert lca(head2, 8, 7) == 1
    assert lca(head2, 3, 0) is None


if __name__ == "__main__":
    test()
