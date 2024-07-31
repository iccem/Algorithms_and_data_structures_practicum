
def convert_naturar2binary(n):
    bn = []
    if n == 0:
        bn.append(0)
        return bn
    else:
        while n > 0:
            bn.append(n % 2)
            n = n // 2
    return bn[::-1]


def read_input():
    n = int(input().strip())
    if n < 0 or n > 10000:
        return -1
    return n


n = read_input()
print("".join(map(str, convert_naturar2binary(n))))
