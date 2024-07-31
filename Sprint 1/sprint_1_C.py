
def find_neighbors(arr, y, x, n, m):
    neighbors = []

    if y-1 >= 0:
        neighbors.append(arr[y-1][x])
    if y+1 <= n-1:
        neighbors.append(arr[y+1][x])
    if x+1 <= m-1:
        neighbors.append(arr[y][x+1])
    if x-1 >= 0:
        neighbors.append(arr[y][x-1])
    return sorted(neighbors)


def read_input():
    arr = []
    n = int(input())
    m = int(input())
    if (n < 0 or n > 1001) or (n < 0 or n > 1001):
        return -1
    counter = n
    while counter > 0:
        arr.append(list(map(int, input().strip().split())))
        counter -= 1
    y = int(input())
    x = int(input())
    if (y < 0 or y > n) or (x < 0 or x > m):
        return -1
    return arr, y, x, n, m


arr, y, x, n, m = read_input()
print(" ".join(map(str, find_neighbors(arr, y, x, n, m))))
