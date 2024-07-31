def get_buble_sort(arr):
    steps = []
    n = len(arr)
    counter = False
    for j in range(1, n):
        for i in range(0, n-j):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                counter = True
        if counter == True:
            steps.append(' '.join(map(str, arr)))
            counter = False
        elif counter == False and j == 1:
            steps.append(' '.join(map(str, arr)))
            return steps
    return steps


def read_input():
    n = input().strip()
    temp = list(map(int, input().strip().split()))
    return temp


unsorted_arr = read_input()
sorted_arr_steps = get_buble_sort(unsorted_arr)
print('\n'.join(map(str, sorted_arr_steps)))
