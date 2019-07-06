def fib_bu(n):
    if n <= 1:
        return n
    prev, curr = 0, 1

    for i in range(n - 2):
        nex = prev + curr
        prev = curr
        curr = nex

    return curr


def test():
    assert fib_bu(5) == 3
    assert fib_bu(6) == 5
    assert fib_bu(7) == 8
    assert fib_bu(13) == 144


if __name__ == "__main__":
    test()
