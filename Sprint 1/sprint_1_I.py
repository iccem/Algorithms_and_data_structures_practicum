def is_power_of_four(number: int) -> bool:
    if number == 1:
        return 'True'
    i = 1
    result = 4
    m = int(number / result)
    for i in range(1, m+2):
        result = 4**i
        if result == number:
            return 'True'
    return 'False'

print(is_power_of_four(int(input())))
