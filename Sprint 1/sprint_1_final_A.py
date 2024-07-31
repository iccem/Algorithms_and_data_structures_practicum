'''
https://contest.yandex.ru/contest/22450/run-report/115047160/
'''


def nearest_zero(arr):
    n = len(arr)
    result = [0] * n
    left = -1
    right = 0
    diff = 0
    mid = 0
    zeros = []
    for i in range(n):
        if arr[i] == 0:
            zeros.append(i)
            if left != -1:
                right = i
                diff = right - left - 1
                if diff > 1:
                    mid = int(diff / 2)
                    m = right - mid
                    for k in range(m, right):
                        result[k] = abs(k - right)
                left = right
            else:
                left = i
        else:
            result[i] = abs(i - left)
    if zeros:
        for j in range(0, zeros[0]):
            result[j] = abs(j - zeros[0])
    return result


def read_input():
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    return arr


def main():
    arr = read_input()
    print(" ".join(map(str, nearest_zero(arr))))


if __name__ == '__main__':
    main()
