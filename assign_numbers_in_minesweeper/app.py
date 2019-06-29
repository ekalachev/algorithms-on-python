def mine_sweeper(bombs, num_rows, num_cols):
    # creates new two-dimensional array initialized by zeros
    field = [[0 for i in range(num_cols)] for j in range(num_rows)]

    for bomb in bombs:
        (bomb_row, bomb_col) = bomb

        field[bomb_row][bomb_col] = -1

        for row in range(bomb_row - 1, bomb_row + 2):
            if row < 0 or row >= num_rows:
                continue
            for col in range(bomb_col - 1, bomb_col + 2):
                if 0 <= col < num_cols and field[row][col] is not -1:
                    field[row][col] += 1

    return field


def test():
    assert mine_sweeper([[0, 2], [2, 0]], 3, 3) == [[0, 1, -1], [1, 2, 1], [-1, 1, 0]]
    assert mine_sweeper([[0, 0], [0, 1], [1, 2]], 3, 4) == [[-1, -1, 2, 1], [2, 3, -1, 1], [0, 1, 1, 1]]
    assert mine_sweeper([[1, 1], [1, 2], [2, 2], [4, 3]], 5, 5) == [[1, 2, 2, 1, 0], [1, -1, -1, 2, 0],
                                                                    [1, 3, -1, 2, 0], [0, 1, 2, 2, 1], [0, 0, 1, -1, 1]]


if __name__ == "__main__":
    test()
