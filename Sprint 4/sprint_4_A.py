
def read_input():
    n = int(input().strip())
    names = {}
    counter = 1
    while n > 0:
        temp = input().strip()
        if temp not in names:
            names[temp] = counter
            counter += 1
        n -= 1
    return names


names = read_input()
print('\n'.join([i for i in names]))
