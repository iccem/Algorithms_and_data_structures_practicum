from typing import List


def factorize(number: int) -> List[int]:
    if number <= 1:
        return [number]
    # if number
    divisors = []
    n = int(number ** 0.5)
    for i in range(2, n):
        while number % i == 0:
            divisors.append(i)
            number = int(number / i)
    if number > 1:
        divisors.append(number)
    return divisors


result = factorize(int(input()))
print(" ".join(map(str, result)))
