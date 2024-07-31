

def sum_binary_numbers (arr1, arr2):
    result = []
    carried = 0

    if len(arr1) != len(arr2):
        a = len(arr1)
        b = len(arr2)
        x = max(a, b)
        if len(arr1) < len(arr2):
            temp = arr1.zfill(x)
            arr1 = temp
        else:
            temp = arr2.zfill(x)
            arr2 = temp

    for i in range(len(arr1)-1, -1, -1):
        if arr1[i] == arr2[i] == '0':
            if carried == 1:
                result.append('1')
                carried = 0
            else:
                result.append('0')
            i -= 1
        elif (arr1[i] == '0' and arr2[i] == '1') or (arr1[i] == '1' and arr2[i] == '0'):
            if carried == 1:
                result.append('0')
            else:
                result.append('1')
            i -= 1
        elif arr1[i] == arr2[i] == '1':
            if carried == 1:
                result.append('1')
            else:
                result.append('0')
                carried = 1
            i -= 1
    if carried == 1:
        result.append('1')
    return (result[::-1])


def read_input():
    arr1 = input().strip()
    arr2 = input().strip()
    return arr1, arr2


arr1, arr2 = read_input()
print("".join(map(str, sum_binary_numbers (arr1, arr2))))
