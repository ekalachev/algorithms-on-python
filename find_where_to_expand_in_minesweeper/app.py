from queue import Queue


# my solution
def click(field, num_rows, num_cols, given_i, given_j):
    find(field, num_rows, num_cols, given_i, given_j)
    return field


def find(field, num_rows, num_cols, row, col):
    if field[row][col] is not 0:
        return

    field[row][col] = -2

    for row_i in range(row - 1, row + 2):
        if row_i < 0 or row_i >= num_rows:
            continue
        for col_i in range(col - 1, col + 2):
            if 0 <= col_i < num_cols:
                find(field, num_rows, num_cols, row_i, col_i)


# solution by author of the course
def click2(field, num_rows, num_cols, given_i, given_j):
    to_check = Queue()

    if field[given_i][given_j] is 0:
        field[given_i][given_j] = -2
        to_check.put((given_i, given_j))
    else:
        return field

    while not to_check.empty():
        (current_i, current_j) = to_check.get()
        for i in range(current_i - 1, current_i + 2):
            if i < 0 or i >= num_rows:
                continue
            for j in range(current_j - 1, current_j + 2):
                if 0 <= j < num_cols and field[i][j] is 0:
                    field[i][j] = -2
                    to_check.put((i, j))

    return field


def test():
    field1 = [[0, 0, 0, 0, 0],
              [0, 1, 1, 1, 0],
              [0, 1, -1, 1, 0]]

    assert click2(field1, 3, 5, 2, 2) == [[0, 0, 0, 0, 0],
                                          [0, 1, 1, 1, 0],
                                          [0, 1, -1, 1, 0]]

    assert click2(field1, 3, 5, 1, 4) == [[-2, -2, -2, -2, -2],
                                          [-2, 1, 1, 1, -2],
                                          [-2, 1, -1, 1, -2]]

    field2 = [[-1, 1, 0, 0],
              [1, 1, 0, 0],
              [0, 0, 1, 1],
              [0, 0, 1, -1]]

    assert click2(field2, 4, 4, 0, 1) == [[-1, 1, 0, 0],
                                          [1, 1, 0, 0],
                                          [0, 0, 1, 1],
                                          [0, 0, 1, -1]]

    assert click2(field2, 4, 4, 1, 3) == [[-1, 1, -2, -2],
                                          [1, 1, -2, -2],
                                          [-2, -2, 1, 1],
                                          [-2, -2, 1, -1]]


if __name__ == '__main__':
    test()
