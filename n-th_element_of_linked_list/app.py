class Node:
    def __init__(self, value, child=None):
        self.value = value
        self.child = child

    def __str__(self):
        return str(self.value)


def nth_from_last(head, n):
    left = head
    right = head

    for i in range(n):
        if right is None:
            return None
        right = right.child

    while right is not None:
        right = right.child
        left = left.child

    if left is None:
        return None

    return left.value


def test():
    current = Node(1)
    for i in range(2, 8):
        current = Node(i, current)
    head = current

    assert nth_from_last(head, 1) == 1
    assert nth_from_last(head, 5) == 5

    current2 = Node(4)
    for i in range(3, 0, -1):
        current2 = Node(i, current2)
    head2 = current2

    assert nth_from_last(head2, 2) == 3
    assert nth_from_last(head2, 4) == 1
    assert nth_from_last(head2, 5) is None
    assert nth_from_last(None, 1) is None


if __name__ == "__main__":
    test()
