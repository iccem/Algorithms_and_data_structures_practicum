def binary_search(arr, x, left, right):
    if right <= left:
        return -1
    mid = (left + right) // 2
    if arr[mid] >= x > arr[mid - 1]:
        return mid
    elif x <= arr[mid]:
        return binary_search(arr, x, left, mid)
    else:
        return binary_search(arr, x, mid + 1, right)


def read_input():
    n = int(input().strip())
    temp = list(map(int, input().strip().split()))
    price = int(input().strip())

    income = [0]
    income.extend(temp)
    max_value = income[-1] + 1
    income.append(max_value)

    prices = [price * i for i in range(1, 3)]
    days = []
    for k in prices:
        result = binary_search(income, k, left=0, right=len(income)-1)
        days.append(result)
    return days


if __name__ == '__main__':
    days = read_input()
    print(" ".join(map(str, days)))
