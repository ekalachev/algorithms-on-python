from bisect import bisect_left


def find_pos(xs, query):
    # Invariant lo <= pos < hi
    lo, hi = 0, len(xs)

    while lo < hi:
        mid = (lo + hi) // 2
        if query < xs[mid]:
            hi = mid        # [lo, mid)
        elif query > xs[mid]:
            lo = mid + 1    # [mid + 1, hi)
        else:
            return mid

    return -1


def find_pos2(xs, query):
    lo = bisect_left(xs, query)
    # i < lo : xs[i] < query
    # i > lo : xs[i] >= query

    if lo < len(xs) and xs[lo] == query:
        return lo
    else:
        return -1


def test():
    assert find_pos([], 100) == -1
    assert find_pos([100], 100) == 0
    assert find_pos([100], 200) == -1
    assert find_pos([1, 4, 7, 9, 22, 77, 102, 555], 9) == 3


def test2():
    assert find_pos2([], 100) == -1
    assert find_pos2([100], 100) == 0
    assert find_pos2([100], 200) == -1
    assert find_pos2([1, 4, 7, 9, 22, 77, 102, 555], 9) == 3


if __name__ == "__main__":
    test()
    test2()
