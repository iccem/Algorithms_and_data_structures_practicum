def calc_quadratic_func(a, x, b, c):
    return a*(x**2) + b*x + c


def read_input():
    temp = list(map(int, input().strip().split()))
    a, x, b, c = temp[0], temp[1], temp[2], temp[3]
    return a, x, b, c


a, x, b, c = read_input()
print(calc_quadratic_func(a, x, b, c))
