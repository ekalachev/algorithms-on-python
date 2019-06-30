def rotate(given_array, n):
    for i in range(n // 2):
        points = init_four_points(i, n)
        swap(given_array, points)
        for j in range(n - 2 - (i * 2)):
            rotate_four_points(points)
            swap(given_array, points)

    return given_array


def init_four_points(i, n):
    return [i, i], [i, n - (i + 1)], [n - (i + 1), n - (i + 1)], [n - (i + 1), i]


def rotate_four_points(points):
    points[0][1] += 1
    points[1][0] += 1
    points[2][1] -= 1
    points[3][0] -= 1


def swap(array, points):
    prev = 0
    for point in points:
        row, col = point
        tmp = array[row][col]
        array[row][col] = prev
        prev = tmp

    array[points[0][0]][points[0][1]] = prev


def test():
    a1 = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

    assert rotate(a1, 3) == [[7, 4, 1],
                             [8, 5, 2],
                             [9, 6, 3]]

    a2 = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

    assert rotate(a2, 4) == [[13, 9, 5, 1],
                             [14, 10, 6, 2],
                             [15, 11, 7, 3],
                             [16, 12, 8, 4]]


if __name__ == "__main__":
    test()
