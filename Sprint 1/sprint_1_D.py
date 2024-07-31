def determine_weather_randomness(arr):
    counter = 0
    if len(arr) == 1:
        return 1
    try:
        if arr[0] > arr[1]:
            counter += 1
        if arr[-1] > arr[-2]:
            counter += 1
        for i in range(1, len(arr)-1):
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                counter += 1
    except ValueError:
        print(-1)
    return counter


def read_input():
    try:
        n = int(input())
        if n < 1 or n > 10**5:
            return -1
        arr = list(map(int, input().strip().split()))
        if len(arr) > n:
            return -1
        if min(arr) < -273 or max(arr) > 273:
            return -1
    except ValueError:
        print(-1)
    return arr


arr = read_input()
print(determine_weather_randomness(arr))
