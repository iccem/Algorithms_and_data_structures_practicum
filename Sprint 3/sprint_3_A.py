
def generate_sequence(current, n):
    if len(current) == n:
        result.append(current)
        return
    else:
        generate_sequence(current + '(', n)
        generate_sequence(current + ')', n)


def is_correct_bracket_sequence(result):
    clear_result = []
    stack = []
    for i in result:
        if i[0] == ')' or i[-1] == '(' or i.count('(') != i.count(')'):
            pass
        elif i.count('(') == i.count(')'):
            for j in i:
                if j == '(':
                    stack.append(j)
                if j == ')' and len(stack) > 0:
                    stack.pop()
            if len(stack) == 0:
                clear_result.append(i)
            stack = []
        else:
            clear_result.append(i)
            stack = []
    return clear_result


def read_input():
    n = int(input().strip())
    return n


current = ''
result = []
n = read_input()
generate_sequence(current, n*2)
clear_result = is_correct_bracket_sequence(result)

print('\n'.join(map(str, clear_result)))
