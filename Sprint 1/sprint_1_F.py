def isPalindrome(txt):
    start = 0
    end = len(txt)-1
    while start < end:
        if txt[start] != txt[end]:
            return 'False'
        start += 1
        end -= 1
    return 'True'


def read_input():
    out = []
    txt = input().lower()
    for i in txt:
        if i.isalnum():
            out.append(i)
    return out


txt = read_input()
print(isPalindrome(txt))
