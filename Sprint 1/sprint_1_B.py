def check_parity(temp):
    if temp[0] % 2 == 0:
        flag = False
    else:
        flag = True
    for i in range(1, len(temp)):
        if (temp[i] % 2 == 0 and flag == True) or (temp[i] % 2 != 0 and flag == False):
            return 'FAIL'
        else:
            pass
    return 'WIN'


def read_input():
    temp = list(map(int, input().strip().split()))
    return temp


temp = read_input()
print(check_parity(temp))
