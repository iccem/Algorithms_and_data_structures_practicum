def is_bigger(a, b):
    if a + b > b + a:
        return True
    else:
        return False


def insertion_sort_by_comparator(array):
    for i in range(1, len(array)):
        buffer = array[i]
        j = i

        while j > 0 and is_bigger(buffer, array[j - 1]):
            array[j] = array[j-1]
            j -= 1
            array[j] = buffer

    return array


def read_input():
    n = input().strip()
    temp = list(input().strip().split())
    return temp


unsorted_arr = read_input()
result = insertion_sort_by_comparator(unsorted_arr)
print(''.join(map(str, result)))

