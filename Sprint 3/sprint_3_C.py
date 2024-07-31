def is_subsequence(s, t):
    i, j = 0, 0
    result = [-1] * len(s)

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            result[i] = j
            i += 1
            j += 1
        else:
            j += 1

    return 'True' if i == len(s) else 'False'


def read_input():
    s = input().strip()
    t = input().strip()
    return s, t


s, t = read_input()
print(is_subsequence(s, t))
