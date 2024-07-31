from typing import Tuple, List


def transpose_matrix(matrix: List[List[int]], n: int, m: int) -> list[List[int]]:
    tmatrix = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            tmatrix[j][i] = matrix[i][j]
    return tmatrix


def read_input() -> Tuple[list[list[int]], int, int]:
    n = int(input().strip())  # rows
    m = int(input().strip())  # cols
    arr = []
    counter = n
    while counter > 0:
        arr.append(list(map(int, input().strip().split())))
        counter -= 1
    return arr, n, m


arr, n, m = read_input()
tmatrix = transpose_matrix(arr, n, m)
print("\n".join(" ".join(map(str, row)) for row in tmatrix))
