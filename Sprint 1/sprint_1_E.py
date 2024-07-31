def find_longest_word(arr):
    counter = 0
    for i in arr:
        temp = len(i)
        if temp > counter:
            counter = temp
            word = i
    return word, counter

def read_input():
    arr = []
    try:
        n = int(input())
        arr = list(input().strip().split())
        if len(arr) == 0:
            return -1
    except ValueError:
        print(-1)
    return arr


arr = read_input()
word, counter = find_longest_word(arr)
print(word)
print(counter)
