
def generate_sequence(sequenses_set, prefix, n, result):
    if n == len(sequenses_set):
        result.append(prefix)
        return
    for i in sequenses_set[n]:
        generate_sequence(sequenses_set, prefix+i, n+1, result)


def read_input():
    out = []
    temp = input().strip()
    for i in temp:
        out.append(int(i))
    return out


def get_code_sequences(sequence_numbers):
    sequenses_set = []
    n = len(sequence_numbers)
    while n > 0:
        for i in sequence_numbers:
            sequenses_set.append(code[i])
            n = n - 1
    return sequenses_set


code = {
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz'
}
prefix = ''
n = 0
result = []

sequence_numbers = read_input()
sequenses_set = get_code_sequences(sequence_numbers)
generate_sequence(sequenses_set, prefix, n, result)
print(' '.join(result))
