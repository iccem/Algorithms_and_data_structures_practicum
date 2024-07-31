from typing import List, Tuple

def get_sum(number_list: List[int], k: int) -> List[int]:
    result = []
    n = len(number_list) - 1
    x = 0
    for i in number_list:
        t = int('1' + '0' * n)
        x += i * t
        n -= 1
    y = str(x + k)
    result = list(map(int, [i for i in y]))
    return result

def read_input() -> Tuple[List[int], int]:
    n = int(input())
    number_list = list(map(int, input().strip().split()))
    k = int(input())
    return number_list, k

number_list, k = read_input()
print(" ".join(map(str, get_sum(number_list, k))))