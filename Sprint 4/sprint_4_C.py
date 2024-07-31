def read_input():
    line1 = input().strip()
    line2 = input().strip()
    n = len(line1)
    alf = {}
    i = 0
    j = 0
    while n > 0:
        if line1[i] not in alf:
            for key, value in alf.items():
                if value == line2[j]:
                    print('NO')
                    return
            alf[line1[i]] = line2[j]
            i += 1
            j += 1
        else:
            key = line1[i]
            temp = alf[key]
            if temp != line2[j]:
                print('NO')
                return
        n -= 1
    if len(line1) == len(line2):
        print('YES')
    else:
        print('NO')

read_input()

