def quick_sort(xs):
    _quick_sort(xs, 0, len(xs) - 1)


def _quick_sort(xs, start, end):
    if start >= end:
        return

    p = partition(xs, start, end)
    _quick_sort(xs, start, p - 1)
    _quick_sort(xs, p + 1, end)


def partition(xs, start, end):
    follower = leader = start
    while leader < end:
        if xs[leader] <= xs[end]:
            xs[follower], xs[leader] = xs[leader], xs[follower]
            follower += 1

        leader += 1
        xs[follower], xs[end] = xs[end], xs[follower]

        return follower


def test():
    # given
    a = [3, 1, 6, 9, 1, 44, 23, 0]

    # when
    quick_sort(a)

    # then
    assert a[0] == 0
    assert a[len(a) - 1] == 44


if __name__ == "__main__":
    test()
