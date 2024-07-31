'''
клумба
'''

def flowerbed_merge_sort(segments):
    result = [segments[0]]
    n = len(segments)
    for i in range(1, n):
        current = segments[i]
        previous = result[-1]

        if current[0] <= previous[1]:
            result[-1] = [previous[0], max(previous[1], current[1])]
        else:
            result.append(current)

    return result

def read_input():
    n = int(input())
    arr = []
    counter = n
    while counter > 0:
        arr.append(list(map(int, input().strip().split())))
        counter -= 1
    arr.sort(key=lambda x: x[0])
    return arr


arrs = read_input()
results = flowerbed_merge_sort(arrs)
for i in results:
    print(' '.join(map(str, i)))
