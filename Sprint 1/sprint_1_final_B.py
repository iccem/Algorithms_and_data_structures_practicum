'''
https://contest.yandex.ru/contest/22450/run-report/115075545/
'''

from collections import defaultdict


def get_points(field, k):
    score = defaultdict(int)
    points = 0
    counter = 0
    for i in field:
        if i.isdigit():
            score[i] += 1
    for j in score:
        value = score[j]
        if 1 <= value <= 2*k:
            points += 1
    return points


def read_input():
    k = int(input())
    field = ''
    i = 4
    while i > 0:
        field += input()
        i -= 1
    return field, k


def main():
    field, k = read_input()
    print(get_points(field, k))


if __name__ == '__main__':
    main()
