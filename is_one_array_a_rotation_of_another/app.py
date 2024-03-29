def is_rotation(list1, list2):
    if len(list1) != len(list2):
        return False

    first = list1[0]
    index2 = -1

    for i in range(len(list2)):
        if list2[i] == first:
            index2 = i
            break

    if index2 == -1:
        return False

    for i in range(len(list1)):
        index2_i = (index2 + i) % len(list2)

        if list1[i] != list2[index2_i]:
            return False

    return True


def test():
    list1 = [1, 2, 3, 4, 5, 6, 7]

    list2a = [4, 5, 6, 7, 8, 1, 2, 3]
    assert is_rotation(list1, list2a) is False

    list2b = [4, 5, 6, 7, 1, 2, 3]
    assert is_rotation(list1, list2b) is True

    list2c = [4, 5, 6, 9, 1, 2, 3]
    assert is_rotation(list1, list2c) is False

    list2d = [4, 6, 5, 7, 1, 2, 3]
    assert is_rotation(list1, list2d) is False

    list2e = [4, 5, 6, 7, 0, 2, 3]
    assert is_rotation(list1, list2e) is False

    list2f = [1, 2, 3, 4, 5, 6, 7]
    assert is_rotation(list1, list2f) is True

    list2g = [7, 1, 2, 3, 4, 5, 6]
    assert is_rotation(list1, list2g) is True


if __name__ == "__main__":
    test()
